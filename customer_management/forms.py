from django.core.urlresolvers import reverse
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from .models import Customer


class CustomerCreateForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomerCreateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.form_action = reverse('customer_add')

        self.helper.form_method = 'POST'
        # self.helper.form_class = 'form-horizontal'

        # set form field properties
        # self.helper.help_text_inline = False
        # self.helper.html5_required = True
        # self.helper.label_class = 'col-sm-2 control-label'
        # self.helper.field_class = 'col-sm-10'

        # add buttons
        # self.helper.layout[-1] = FormActions(
        #     Submit('add_button', 'Submit', css_class="btn btn-pri mary"),
        #     Submit('cancel_button', u'Скасувати', css_class="btn btn -link"),
        # )

        self.helper.add_input(Submit('submit', 'Submit'))
