from django.apps import AppConfig


# signals for stripe
class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals
