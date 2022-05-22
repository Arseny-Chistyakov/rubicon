from django import forms

from blogs.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({'class': 'form-control autosize'})
        self.fields['name'].widget.attrs.update({'class': 'form-control py-4'})
