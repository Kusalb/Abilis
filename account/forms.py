from django import forms
# from multiselectfield import MultiSelectFormField

from .models import Documentation, Category, DocumentCategory, Form_answer



class DocumentationForm(forms.ModelForm):
    class Meta:
        model = Documentation
        fields = ('title', 'date', 'doc_category', 'document', 'description', 'information', 'info_file')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('new_category',)


class DocumentNewForm(forms.ModelForm):
    class Meta:
        model = DocumentCategory
        fields = ('doc_category',)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Form_answer
        fields = ('answer', )


class UserSearchForm(forms.Form):
    user_column = forms.CharField(max_length=222)
    keyword_user = forms.CharField(max_length=222)


class DocumentSearchForm(forms.Form):
    document_column = forms.CharField(max_length=222)
    keyword_document = forms.CharField(max_length=222)


class QuestionSearchForm(forms.Form):
    question_column = forms.CharField(max_length=222)
    keyword_question = forms.CharField(max_length=222)



class AnswerSearchForm(forms.Form):
    answer_column = forms.CharField(max_length=222)
    keyword_answer = forms.CharField(max_length=222)


