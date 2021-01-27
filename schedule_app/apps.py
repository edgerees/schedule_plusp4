from django.apps import AppConfig


class ScheduleAppConfig(AppConfig):
    name = 'schedule_app'

    def ready(self):
        import schedule_app.signals
