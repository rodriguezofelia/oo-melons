"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    
    def __init__(self, species, qty, shipped, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = shipped
        self.order_type = order_type
        self.tax = tax

    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "christmas melon":
            base_price *= 1.5
            
        total = (1 + self.tax) * self.qty * base_price
        
        if self.order_type == "international" and self.qty < 10: 
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder): 
    """A government melon order with no taxes."""
    tax = 0
    passed_inspection = False

    def mark_inspection(passed):
        if passed: 
            self.passed_inspection = True

# An example order to test our functions
order = GovernmentMelonOrder("christmas melon", 1, True, "domestic", 0)

# Prints order total
print(order.get_total())