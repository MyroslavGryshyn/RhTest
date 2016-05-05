from django.core.urlresolvers import reverse
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import StrictButton

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
        self.helper.form_class = 'form-horizontal'

        # Setting form properties
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'

        # add button
        self.helper.add_input(Submit('submit', 'Submit',
                                     css_class='btn-primary'))


class CustomerUpdateForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomerUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.form_action = reverse('customer_edit',
            kwargs={'pk': kwargs['instance'].id})

        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # Setting form properties
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'

        # add button
        self.helper.add_input(Submit('submit', 'Submit',
                                     css_class='btn-primary'))
