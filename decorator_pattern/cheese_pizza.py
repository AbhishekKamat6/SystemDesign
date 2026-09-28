from decorator_v1 import Decorator


class CheesePizza(Decorator):


    @property
    def cost(self):
        return self.inner.cost + 20

    @property
    def desc(self):
        return self.inner.desc + "extra cheese"