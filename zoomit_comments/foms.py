from django import forms


class UserCommentForm(forms.Form):
    post = forms.CharField(
        widget=forms.HiddenInput()
    )

    body = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'نظر خود را بنویسید'})
    )


class UserCommentReplyForm(forms.Form):
    body = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'reply-text-area', 'rows': '2'})
    )
