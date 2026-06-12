from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario", max_length=150)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
    tipo_usuario = forms.ChoiceField(
        label="Entrar como",
        choices=[
            ("anfitriao", "Anfitriao"),
            ("hospede", "Hospede"),
        ],
    )


class CadastroForm(forms.Form):
    tipo_usuario = forms.ChoiceField(
        label="Cadastrar como",
        choices=[
            ("anfitriao", "Anfitriao"),
            ("hospede", "Hospede"),
        ],
    )
    username = forms.CharField(label="Usuario", max_length=150)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
    nome = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="Email")
    telefone = forms.CharField(label="Telefone", max_length=20)
    cpf = forms.CharField(label="CPF", max_length=14)
    data_nascimento = forms.DateField(
        label="Data de nascimento",
        widget=forms.DateInput(attrs={"type": "date"}),
    )