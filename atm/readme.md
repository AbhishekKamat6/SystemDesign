

# design atm

## requirements

1) there is a customer
2) custome will insert a card
3) will authenticate using pin 
4) withdraw cash
5) deposit money
6) or check their balance

## other requirements

1) bank should verify every transaction
2) dispense right mix of notes 
3) return card
4) stay correct when things fail midway

## functional requirements

1) Insert card
2) Authenticate
3) Withdraw
4) Deposit
5) Balance enquiry
6) Dispense correct notes
7) cancel and eject 
8) operator --> refill note cassettes and audit the cash held

## non-functional requirements

1) security
2) correctness of money movement
3) extensibility
4) availability
5) thread safety

## clarifying questions

1) Denominations -: which notes(100,200,500) does machine hold ? and is amount restricted ?
2) PIN policy -: How many attempts ? and is card retained after last failues
3) Limits -: Is there any withdrawl limit
4) Accounts: one account per card, or can a card select between accounts? means one card can have mutiple accounts ( Current account or Saving account  )

# Assumed answers for this design: 

withdraw, deposit, and balance inquiry; notes of 2000, 500, and 100 with amounts in multiples of 100; three PIN attempts then the card is retained; a daily limit enforced by the bank; the bank is authoritative and reachable; one account per card; receipts noted as an extension.









# INSIGHTS 

FastAPI Multiple Workers and Shared Sessions
1. The Problem with In-Memory Sessions

Suppose we store sessions like this:

sessions: dict[str, ATM] = {}

This works when the FastAPI application has only one worker.

Customer
   |
   ↓
FastAPI Worker
   |
   ↓
sessions = {
    "ABC123": ATM(...)
}

The worker knows about the session because the session is stored in its local Python memory.

2. What Happens with Multiple Workers?

When FastAPI runs with multiple workers, there are multiple separate Python processes.

For example:

                 Load Balancer
                      |
          ┌───────────┼───────────┐
          ↓           ↓           ↓
       Worker 1    Worker 2    Worker 3
          |           |           |
     sessions={} sessions={} sessions={}

Each worker has its own copy of:

sessions = {}

They do not automatically share Python variables.

Example

Customer inserts a card.

The request goes to Worker 1:

Customer
   |
   ↓
Worker 1
   |
   ↓
sessions["ABC123"] = ATM(...)

Now:

Worker 1:
sessions = {
    "ABC123": ATM(...)
}

Worker 2:
sessions = {}

Worker 3:
sessions = {}

The session exists only inside Worker 1's memory.

3. The Next Request Can Go to Another Worker

The customer now enters their PIN:

POST /atm/enter-pin
X-Session-ID: ABC123

The request might be sent to Worker 2:

Customer
   |
   ↓
Load Balancer
   |
   ↓
Worker 2

Worker 2 checks:

sessions["ABC123"]

But Worker 2 has:

sessions = {}

Therefore the session cannot be found.

SessionNotFoundException

Even though Worker 1 has the session.

4. Multiple Workers Do Not Mean Requests Are Always Parallel

Having multiple workers means we have multiple independent processes that can handle multiple requests concurrently.

For example:

Request A ──→ Worker 1
Request B ──→ Worker 2
Request C ──→ Worker 3

These requests can be processed at the same time.

But multiple workers do not mean every endpoint is automatically called in parallel.

5. Using Redis for Shared Session State

Instead of keeping sessions in each worker's local memory:

sessions = {}

we can store session data in Redis.

                 Redis
                   ↑
                   |
          ┌────────┼────────┐
          ↓        ↓        ↓
       Worker 1 Worker 2 Worker 3

Now all workers access the same shared session store.

Example

Worker 1 receives the card insertion:

Worker 1
   |
   ↓
Redis

ABC123 → {
    card: CARD-1,
    state: CARD_INSERTED
}

Later, Worker 3 receives the PIN request:

Worker 3
   |
   ↓
Redis
   |
   ↓
ABC123
   |
   ↓
state = CARD_INSERTED

Worker 3 can therefore continue the same session.

6. Important: Redis Doesn't Store the Python ATM Object

We generally should not think of Redis as storing:

ABC123 → Python ATM object

Instead, Redis stores serializable session information/state:

ABC123 → {
    card_id: CARD-1,
    account_id: ACC-1,
    state: CARD_INSERTED
}

The important idea is:

Redis provides a common/shared place where all workers can store and retrieve session state.

7. ATM Example

Without Redis:

Customer
   ↓
Worker 1
   ↓
Local sessions
   ↓
ABC123 → ATM

If the next request goes to Worker 2:

Customer
   ↓
Worker 2
   ↓
Local sessions
   ↓
ABC123 not found ❌

With Redis:

Customer
   ↓
Worker 1
   ↓
Redis
   ↓
ABC123 → session data

Next request:

Customer
   ↓
Worker 2
   ↓
Redis
   ↓
ABC123 → session data
   ↓
Continue session ✅
Key Takeaway
Local Python variable
        ↓
Belongs to one worker/process

Redis
        ↓
Shared storage accessible by all workers

Therefore, when running a multi-worker FastAPI application, shared state such as sessions should not be kept only in a local Python dictionary if requests need to work regardless of which worker receives them.