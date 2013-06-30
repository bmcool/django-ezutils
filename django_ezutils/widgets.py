
from django.forms.widgets import DateInput

from django.contrib.admin.templatetags.admin_static import static

class DatePickerWidget(DateInput):
    class Media:
        css = {
            "all": (
                static("css/cupertino/jquery-ui-1.10.3.custom.css"),
            )
        }
        js = (
            static("js/jqcalendar.js"),
            static("js/jquery-ui-1.10.3.custom.js"),
        )
    
    def __init__(self, *args, **kwargs):        
        super(DatePickerWidget, self).__init__(*args, **kwargs)
        self.attrs = {'class': 'datepicker'}
