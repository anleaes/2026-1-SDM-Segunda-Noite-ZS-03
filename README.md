```plantuml
@startuml ModeloHospedagem

class Usuario {
 -idPessoa: int
 -nome: String
 -email: String
 -senha: String
 +toString()
}

class Hospede {
 -idHospede: int
 -cpf: String
 -Data_de_nascimento: date
 -telefone: String
 -usuario: OneToOne[Usuario]
 +fazer_reserva()
}

class Anfitriao {
 -idAnfitriao: int
 -cpf: String [0..1]
 -cnpj: String [0..1]
 -usuario: OneToOne[Usuario]
 -conta_bancaria: String
 -Data_de_cadastro: date
 -avaliacao_media: Float
 -experied_date: date
 -verified_at: timestamp
 
 +cadastrar_imovel()
}

class Hospedagem {
 -id_hospedagem: int
 -titulo: String
 -descricao: Text
 -preco_noite: Decimal
 -capacidade: Int
 -status: Boolean
 -locador: ForeignKey[Anfritriao]
 -endereco: OneToOne[Endereco]
 +verificar_disponibilidade()
}

class Endereco {
 -logradouro: String
 -rua: String
 -numero: String
 -complemento: String
 -cidade: String
 -estado: String
 -cep: String
}

class Comodidade {
 -idComodidade: int
 -nome: String
 -categoria: String
 -disponivel: boolean
}

class Reserva {
 -id_reserva: int
 -data_entrada: Date
 -data_saida: Date
 -status: CharChoices
 -valor_total: Decimal
 -hospede: ForeignKey[Hospede]
 -hospedagem: ForeignKey[Hospedagem]
 +cancelar()
}

class Pagamento {
 -metodo: enum
 -status: enum
 -data_pagamento: DateTime
 -quantidade_de_parcelas: int
 -reserva: OneToOne[Reserva]
 +processar()
}

class Avaliacao {
 -nota: Integer
 -comentario: Text
 -data: Date
 -reserva: OneToOne[Reserva]
}

class Mensagem{
 -id_mensagem: int
 -conteudo: String
 -Data_envio: date
 -visualizado: boolean
 -id_pessoa: int
}

' Relacionamentos
Hospede -up-|> Usuario
Anfitriao -up-|> Usuario
Hospedagem *-- Endereco : 1..1
Anfitriao "1" --* "n" Hospedagem
Hospedagem "n" *-- "n" Reserva
Hospede "1" *-- "n" Reserva
Reserva "1" -- "1" Pagamento
Reserva "1" -- "0..1" Avaliacao
Hospedagem "n" -- "n" Comodidade
Hospede "1" *-- "n" Mensagem
Anfitriao "1" *-- "n" Mensagem

@enduml
