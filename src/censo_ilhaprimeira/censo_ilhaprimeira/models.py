from django.db import models

class Morador(models.Model):
    
    ESCOLHAS_SEXO = [
        ("MASCULINO", "1 - MASCULINO"),
        ("FEMININO", "2 - FEMININO")
    ]

    ESCOLHAS_RELACAO = [
        ("PESSOA RESPONSÁVEL PELO DOMICÍLIO", "01 - PESSOA RESPONSÁVEL PELO DOMICÍLIO"),
        ("CÔNJUGE OU COMPANHEIRO(A) DE SEXO DIFERENTE", "02 - CÔNJUGE OU COMPANHEIRO(A) DE SEXO DIFERENTE"),
        ("CÔNJUGE OU COMPANHEIRO(A) DO MESMO SEXO", "03 - CÔNJUGE OU COMPANHEIRO(A) DO MESMO SEXO"),
        ("FILHO(A) DO RESPONSÁVEL E DO CÔNJUGE", "04 - FILHO(A) DO RESPONSÁVEL E DO CÔNJUGE"),
        ("FILHO(A) SOMENTE DO RESPONSÁVEL", "05 - FILHO(A) SOMENTE DO RESPONSÁVEL"),
        ("ENTEADO(A)", "06 - ENTEADO(A)"),
        ("GENRO OU NORA", "07 - GENRO OU NORA"),
        ("PAI, MÃE, PADRASTO OU MADRASTA", "08 - PAI, MÃE, PADRASTO OU MADRASTA"),
        ("SOGRO(A)", "09 - SOGRO(A)"),
        ("NETO(A)", "10 - NETO(A)"),
        ("BISNETO(A)", "11 - BISNETO(A)"),
        ("IRMÃO OU IRMÃ", "12 - IRMÃO OU IRMÃ"),
        ("AVÔ OU AVÓ", "13 - AVÔ OU AVÓ"),
        ("OUTRO PARENTE", "14 - OUTRO PARENTE"),
        ("AGREGADO(A)", "15 - AGREGADO(A)"),
        ("PENSIONISTA", "17 - PENSIONISTA"),
        ("EMPREGADO(A) DOMÉSTICO(A)", "18 - EMPREGADO(A) DOMÉSTICO(A)"),
        ("PARENTE DO(A) EMPREGADO(A) DOMÉSTICO(A)", "19 - PARENTE DO(A) EMPREGADO(A) DOMÉSTICO(A)"),
        ("INDIVIDUAL EM DOMICÍLIO COLETIVO", "20 - INDIVIDUAL EM DOMICÍLIO COLETIVO"),
    ]

    ESCOLHAS_COR = [
        ("BRANCA", "1 - BRANCA"),
        ("PRETA", "2 - PRETA"),
        ("AMARELA", "3 - AMARELA"),
        ("PARDA", "4 - PARDA"),
        ("INDÍGENA", "5 - INDÍGENA"),
    ]

    ESCOLHAS_REGISTRO_NASCIMENTO = [
        ("DO CARTÓRIO", "1 - DO CARTÓRIO"),
        ("REGISTRO ADMINISTRATIVO DE NASCIMENTO INDÍGENA (RANI)", "2 - REGISTRO ADMINISTRATIVO DE NASCIMENTO INDÍGENA (RANI)"),
        ("NÃO TEM", "3 - NÃO TEM"),
        ("NÃO SABE", "4 - NÃO SABE"),
    ]

    ESCOLHAS_RENDIMENTO_BRUTO_RESPONSAVEL = [
        ("VALOR EM DINHEIRO, PRODUTOS OU MERCADORIAS", "1 - VALOR EM DINHEIRO, PRODUTOS OU MERCADORIAS"),
        ("OUTRA FORMA (MORADIA, ALIMENTAÇÃO, TREINAMENTO ETC.)", "2 - OUTRA FORMA (MORADIA, ALIMENTAÇÃO, TREINAMENTO ETC.)"),
        ("NÃO TEM", "3 - NÃO TEM"),
    ]

    ESCOLHAS_PRESTADOR_INFORMACOES = [
        ("A PRÓPRIA PESSOA", "1 - A PRÓPRIA PESSOA"),
        ("OUTRO MORADOR", "2 - OUTRO MORADOR"),
        ("NÃO MORADOR", "3 - NÃO MORADOR"),
    ]

    ESCOLHAS_FAIXA_RENDIMENTO_RESPONSAVEL = [
        ("1,00 A 500,00", "1 - 1,00 A 500,00"),
        ("501,00 A 1.000,00", "2 - 501,00 A 1.000,00"),
        ("1.001,00 A 2.000,00", "3 - 1.001,00 A 2.000,00"),
        ("2.001,00 A 3.000,00", "4 - 2.001,00 A 3.000,00"),
        ("3.001,00 A 5.000,00", "5 - 3.001,00 A 5.000,00"),
        ("5.001,00 A 10.000,00", "6 - 5.001,00 A 10.000,00"),
        ("10.001,00 A 20.000,00", "7 - 10.001,00 A 20.000,00"),
        ("20.001,00 A 100.000", "8 - 20.001,00 A 100.000"),
        ("100.001 OU MAIS", "9 - 100.001 OU MAIS"),
    ]


    # Primeira folha
    cpf = models.CharField(primary_key=True, null=False, max_length=11)
    nome = models.CharField(max_length=35)
    sobrenome = models.CharField(max_length=200)
    email = models.EmailField(max_length=244)
    telefone_fixo = models.CharField(null=True, blank=True)
    telefone_movel = models.CharField(null=True, blank=True)
    sexo = models.TextField(choices=ESCOLHAS_SEXO, null=True, blank=True)
    dt_nascimento = models.DateField(null=True, blank=True)
    idade_anos = models.IntegerField(null=True, blank=True)
    idade_meses = models.IntegerField(null=True, blank=True)
    relacao_parentesco_responsavel = models.TextField(choices=ESCOLHAS_RELACAO, null=True, blank=True)

    # Segunda folha
    cor = models.TextField(choices=ESCOLHAS_COR)
    se_considera_indigena = models.BooleanField()
    etnia1 = models.CharField(max_length=20, null=True, blank=True)
    etnia2 = models.CharField(max_length=20, null=True, blank=True)
    fala_lingua_indigena_domicilio = models.BooleanField()
    lingua_indigina1 = models.CharField(max_length=20, null=True, blank=True)
    lingua_indigina2 = models.CharField(max_length=20, null=True, blank=True)
    lingua_indigina3 = models.CharField(max_length=20, null=True, blank=True)
    fala_portugues_domicilio = models.BooleanField()
    se_considera_quilombola = models.BooleanField(null=True, blank=True)
    nome_comunidade_quilombola = models.CharField(max_length=50, null=True, blank=True)
    registro_nascimento = models.TextField(choices=ESCOLHAS_REGISTRO_NASCIMENTO)
    sabe_ler_escrever = models.BooleanField()
    
    # Terceira folha
    rendimento_bruto_responsavel = models.TextField(choices=ESCOLHAS_RENDIMENTO_BRUTO_RESPONSAVEL, null=True, blank=True)
    valor_rendimento_responsavel = models.FloatField(null=True, blank=True)
    faixa_rendimento_responsavel = models.TextField(choices=ESCOLHAS_FAIXA_RENDIMENTO_RESPONSAVEL, null=True, blank=True)
    quem_prestou_info = models.TextField(choices=ESCOLHAS_PRESTADOR_INFORMACOES)
    nome_outro_morador = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return f'{self.cpf} - {self.nome} - {self.domicilio_relacionado}'

class Domicilio(models.Model):

    ESCOLHAS_ESPECIEDOMICILIO = [
        ("DOMICÍLIO PARTICULAR PERMANENTE OCUPADO", "1 - DOMICÍLIO PARTICULAR PERMANENTE OCUPADO"),
        ("DOMICÍLIO PARTICULAR IMPROVISADO OCUPADO", "5 - DOMICÍLIO PARTICULAR IMPROVISADO OCUPADO"),
        ("DOMICÍLIO COLETIVO COM MORADOR", "6 - DOMICÍLIO COLETIVO COM MORADOR")
    ]
    
    ESCOLHAS_TIPO = [
        ("CASA", "011 - CASA"),
        ("CASA DE VILA OU EM CONDOMÍNIO", "012 - CASA DE VILA OU EM CONDOMÍNIO"),
        ("APARTAMENTO", "013 - APARTAMENTO"),
        ("HABITAÇÃO EM CASA DE CÔMODOS OU CORTIÇO", "014 - HABITAÇÃO EM CASA DE CÔMODOS OU CORTIÇO"),
        ("HABITAÇÃO INDÍGENA SEM PAREDES OU MALOCA", "015 - HABITAÇÃO INDÍGENA SEM PAREDES OU MALOCA"),
        ("ESTRUTURA RESIDENCIAL PERMANENTE DEGRADADA OU INACABADA", "106 - ESTRUTURA RESIDENCIAL PERMANENTE DEGRADADA OU INACABADA"),
        ("TENDA OU BARRACA DE LONA, PLÁSTICO OU TECIDO", "051 - TENDA OU BARRACA DE LONA, PLÁSTICO OU TECIDO"),
        ("DENTRO DO ESTABELECIMENTO EM FUNCIONAMENTO", "052 - DENTRO DO ESTABELECIMENTO EM FUNCIONAMENTO"),
        ("OUTROS (ABRIGOS NATURAIS E OUTRAS ESTRUTURAS IMPROVISADAS)", "053 - OUTROS (ABRIGOS NATURAIS E OUTRAS ESTRUTURAS IMPROVISADAS)"),
        ("ESTRUTURA IMPROVISADA EM LOGRADOURO PÚBLICO, EXCETO TENDA OU BARRACA", "504 - ESTRUTURA IMPROVISADA EM LOGRADOURO PÚBLICO, EXCETO TENDA OU BARRACA"),
        ("ESTRUTURA NÃO RESIDENCIAL PERMANENTE DEGRADADA OU INACABADA", "505 - ESTRUTURA NÃO RESIDENCIAL PERMANENTE DEGRADADA OU INACABADA"),
        ("VEÍCULOS (CARROS, CAMINHÕES, TRAILERS, BARCOS ETC.)", "506 - VEÍCULOS (CARROS, CAMINHÕES, TRAILERS, BARCOS ETC.)"),
        ("ASILOS OU OUTRA INSTITUIÇÃO DE LONGA PERMANÊNCIA PARA IDOSOS", "061 - ASILO OU OUTRA INSTITUIÇÃO DE LONGA PERMANÊNCIA PARA IDOSOS"),
        ("HOTEL OU PENSÃO", "062 - HOTEL OU PENSÃO"),
        ("ALOJAMENTO", "063 - ALOJAMENTO"),
        ("PENITENCIÁRIA, CENTRO DE DETENÇÃO E SIMILAR", "064 - PENITENCIÁRIA, CENTRO DE DETENÇÃO E SIMILAR"),
        ("OUTRO", "065 - OUTRO"),
        ("ABRIGO, ALBERGUE OU CASA DE PASSAGEM PARA POPULAÇÃO EM SITUAÇÃO DE RUA", "606 - ABRIGO, ALBERGUE OU CASA DE PASSAGEM PARA POPULAÇÃO EM SITUAÇÃO DE RUA"),
        ("ABRIGO, CASAS DE PASSAGEM OU REPÚBLICA ASSISTENCIAL PARA OUTROS GRUPOS VULNERÁVEIS", "607 - ABRIGO, CASAS DE PASSAGEM OU REPÚBLICA ASSISTENCIAL PARA OUTROS GRUPOS VULNERÁVEIS"),
        ("CLÍNICA PSIQUIÁTRICA, COMUNIDADE TERAPÊUTICA E SIMILAR", "608 - CLÍNICA PSIQUIÁTRICA, COMUNIDADE TERAPÊUTICA E SIMILAR"),
        ("ORFANATO E SIMILAR", "609 - ORFANATO E SIMILAR"),
        ("UNIDADE DE INTERNAÇÃO DE MENORES", "610 - UNIDADE DE INTERNAÇÃO DE MENORES"),
        ("QUARTEL OU OUTRA ORGANIZAÇÃO MILITAR", "611 - QUARTEL OU OUTRA ORGANIZAÇÃO MILITAR")
    ]

    ESCOLHAS_ABASTECIMENTO = [
        ("REDE GERAL DE DISTRIBUIÇÃO", "1 - REDE GERAL DE DISTRIBUIÇÃO"),
        ("PROFUNDO OU ARTESIANO", "2 - PROFUNDO OU ARTESIANO"),
        ("RASO, FREÁTICO OU CACIMBA", "3 - RASO, FREÁTICO OU CACIMBA"),
        ("FONTE, NASCENTE OU MINA", "4 - FONTE, NASCENTE OU MINA"),
        ("CARRO-PIPA", "5 - CARRO-PIPA"),
        ("ÁGUA DA CHUVA ARMAZENADA", "6 - ÁGUA DA CHUVA ARMAZENADA"),
        ("RIOS, AÇUDES, CÓRREGOS, LAGOS E IGARAPÉS", "7 - RIOS, AÇUDES, CÓRREGOS, LAGOS E IGARAPÉS"),
        ("OUTRA", "8 - OUTRA"),
    ]

    ESCOLHAS_AGUA_CHEGA = [
        ("ENCANADA ATÉ DENTRO DA CASA, APARTAMENTO OU HABITAÇÃO", "1 - ENCANADA ATÉ DENTRO DA CASA, APARTAMENTO OU HABITAÇÃO"),
        ("ENCANADA, MAS APENAS NO TERRENO", "2 - ENCANADA, MAS APENAS NO TERRENO"),
        ("NÃO CHEGA ENCANADA", "3 - NÃO CHEGA ENCANADA"),
    ]

    ESCOLHAS_ESGOTO_BANHEIRO = [
        ("REDE GERAL OU PLUVIAL", "1 - REDE GERAL OU PLUVIAL"),
        ("LIGADA À REDE", "2 - LIGADA À REDE"),
        ("NÃO LIGADA À REDE", "3 - NÃO LIGADA À REDE"),
        ("FOSSA RUDIMENTAR OU BURACO", "4 - FOSSA RUDIMENTAR OU BURACO"),
        ("VALA", "5 - VALA"),
        ("RIO, LAGO, CÓRREGO OU MAR", "6 - RIO, LAGO, CÓRREGO OU MAR"),
        ("OUTRA FORMA", "7 - OUTRA FORMA"),
    ]

    ESCOLHAS_ESGOTO_SAN_BUR = [
        ("REDE GERAL OU PLUVIAL", "1 - REDE GERAL OU PLUVIAL"),
        ("LIGADA À REDE", "2 - LIGADA À REDE"),
        ("NÃO LIGADA À REDE", "3 - NÃO LIGADA À REDE"),
        ("FOSSA RUDIMENTAR OU BURACO", "4 - FOSSA RUDIMENTAR OU BURACO"),
        ("VALA", "5 - VALA"),
        ("RIO, LAGO, CÓRREGO OU MAR", "6 - RIO, LAGO, CÓRREGO OU MAR"),
        ("OUTRA FORMA", "7 - OUTRA FORMA"),
    ]

    ESCOLHAS_LIXO_DOMICILIO = [
        ("COLETADO NO DOMICÍLIO POR SERVIÇO DE LIMPEZA", "1 - COLETADO NO DOMICÍLIO POR SERVIÇO DE LIMPEZA"),
        ("DEPOSITADO EM CAÇAMBA DE SERVIÇO DE LIMPEZA", "2 - DEPOSITADO EM CAÇAMBA DE SERVIÇO DE LIMPEZA"),
        ("QUEIMADO NA PROPRIEDADE", "3 - QUEIMADO NA PROPRIEDADE"),
        ("ENTERRADO NA PROPRIEDADE", "4 - ENTERRADO NA PROPRIEDADE"),
        ("JOGADO EM TERRENO BALDIO, ENCOSTA OU ÁREA PÚBLICA", "5 - JOGADO EM TERRENO BALDIO, ENCOSTA OU ÁREA PÚBLICA"),
        ("OUTRO DESTINO", "6 - OUTRO DESTINO"),
    ]

    ESCOLHAS_RUA = [
        ("R. Marina do Sol", "R. Marina do Sol"),
        ("R. Marina do Frade", "R. Marina do Frade"),
        ("R. Marina dos Coqueiros", "R. Marina dos Coqueiros"),
        ("R. Marina da Lua", "R. Marina da Lua"),
        ("R. Marina do Bosque", "R. Marina do Bosque"),
        ("R. Marina Porto Bali", "R. Marina Porto Bali"),
        ("R. Marina das Flores", "R. Marina das Flores"),
        ("R. Marina das Estrelas", "R. Marina das Estrelas"),
        ("R. Marina Ponta Leste", "R. Marina Ponta Leste")
    ]

    # Relacionamentos
    responsavel = models.ForeignKey(Morador, null=True, on_delete=models.SET_NULL)
    
    # Principais
    id = models.AutoField(primary_key=True)
    uf = models.CharField(max_length=2)
    rua_domicilio = models.TextField(choices=ESCOLHAS_RUA, null=True, blank=True)
    municipio = models.CharField(max_length=5)
    distrito = models.CharField(max_length=2)
    subdistrito = models.CharField(max_length=2)
    setor = models.CharField(max_length=4)
    num_quadra = models.CharField(max_length=3)
    num_face = models.CharField(max_length=3)
    seq_endereco = models.CharField(max_length=6)
    seq_coletivo = models.CharField(max_length=6)
    seq_especie = models.CharField(max_length=6)
    especie_domicilio = models.TextField(choices=ESCOLHAS_ESPECIEDOMICILIO, null=True, blank=True)
    tipo = models.TextField(choices=ESCOLHAS_TIPO, null=True, blank=True)

    # Características Adicionais
    qtd_moradores = models.IntegerField()
    qtd_zeroanove = models.IntegerField()
    forma_abastecimento = models.TextField(choices=ESCOLHAS_ABASTECIMENTO, null=True, blank=True)
    tem_acesso_rede_agua_geral = models.BooleanField(null=True, blank=True)
    como_agua_chega = models.TextField(choices=ESCOLHAS_AGUA_CHEGA, null=True, blank=True)
    num_banheiros_exclusivos = models.IntegerField(null=True, blank=True)
    usa_banheiro_uso_comum = models.BooleanField(null=True, blank=True)
    usa_sanitario_buraco_dejecoes = models.BooleanField(null=True, blank=True)
    esgoto_banheiro = models.TextField(choices=ESCOLHAS_ESGOTO_BANHEIRO, null=True, blank=True)
    esgoto_sanitario_buraco = models.TextField(choices=ESCOLHAS_ESGOTO_SAN_BUR, null=True, blank=True)
    lixo_domicilio = models.TextField(choices=ESCOLHAS_LIXO_DOMICILIO, null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.responsavel} - {self.seq_endereco}'

class Falecido(models.Model):

    ESCOLHAS_SEXO = [
        ("MASCULINO", "1 - MASCULINO"),
        ("FEMININO", "2 - FEMININO")
    ]

    ESCOLHAS_MES_ANO_FALECIMENTO = [
        ("JULHO 2022", "1 - JULHO 2022"),
        ("JUNHO 2022", "2 - JUNHO 2022"),
        ("MAIO 2022", "3 - MAIO 2022"),
        ("ABRIL 2022", "4 - ABRIL 2022"),
        ("MARÇO 2022", "5 - MARÇO 2022"),
        ("FEVEREIRO 2022", "6 - FEVEREIRO 2022"),
        ("JANEIRO 2022", "7 - JANEIRO 2022"),
        ("DEZEMBRO 2021", "8 - DEZEMBRO 2021"),
        ("NOVEMBRO 2021", "9 - NOVEMBRO 2021"),
        ("OUTUBRO 2021", "10 - OUTUBRO 2021"),
        ("SETEMBRO 2021", "11 - SETEMBRO 2021"),
        ("AGOSTO 2021", "12 - AGOSTO 2021"),
        ("JULHO 2021", "13 - JULHO 2021"),
        ("JUNHO 2021", "14 - JUNHO 2021"),
        ("MAIO 2021", "15 - MAIO 2021"),
        ("ABRIL 2021", "16 - ABRIL 2021"),
        ("MARÇO 2021", "17 - MARÇO 2021"),
        ("FEVEREIRO 2021", "18 - FEVEREIRO 2021"),
        ("JANEIRO 2021", "19 - JANEIRO 2021"),
        ("DEZEMBRO 2020", "20 - DEZEMBRO 2020"),
        ("NOVEMBRO 2020", "21 - NOVEMBRO 2020"),
        ("OUTUBRO 2020", "22 - OUTUBRO 2020"),
        ("SETEMBRO 2020", "23 - SETEMBRO 2020"),
        ("AGOSTO 2020", "24 - AGOSTO 2020"),
        ("JULHO 2020", "25 - JULHO 2020"),
        ("JUNHO 2020", "26 - JUNHO 2020"),
        ("MAIO 2020", "27 - MAIO 2020"),
        ("ABRIL 2020", "28 - ABRIL 2020"),
        ("MARÇO 2020", "29 - MARÇO 2020"),
        ("FEVEREIRO 2020", "30 - FEVEREIRO 2020"),
        ("JANEIRO 2020", "31 - JANEIRO 2020"),
        ("DEZEMBRO 2019", "32 - DEZEMBRO 2019"),
        ("NOVEMBRO 2019", "33 - NOVEMBRO 2019"),
        ("OUTUBRO 2019", "34 - OUTUBRO 2019"),
        ("SETEMBRO 2019", "35 - SETEMBRO 2019"),
        ("AGOSTO 2019", "36 - AGOSTO 2019"),
        ("JULHO 2019", "37 - JULHO 2019"),
        ("JUNHO 2019", "38 - JUNHO 2019"),
        ("MAIO 2019", "39 - MAIO 2019"),
        ("ABRIL 2019", "40 - ABRIL 2019"),
        ("MARÇO 2019", "41 - MARÇO 2019"),
        ("FEVEREIRO 2019", "42 - FEVEREIRO 2019"),
        ("JANEIRO 2019", "43 - JANEIRO 2019"),
    ]

    domicilio_relacionado = models.OneToOneField(Domicilio, on_delete=models.CASCADE)
    faleceu_no_periodo = models.BooleanField()
    nome_falecido = models.CharField(max_length=35)
    sobrenome_falecido = models.CharField(max_length=200)
    mes_ano_falecimento = models.TextField(choices=ESCOLHAS_MES_ANO_FALECIMENTO, null=True, blank=True)
    sexo_falecido = models.TextField(choices=ESCOLHAS_SEXO, null=True, blank=True)
    idade_anos_falecimento = models.IntegerField(null=True, blank=True)
    idade_meses_falecimento = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome_falecido} - {self.domicilio_relacionado} - {self.mes_ano_falecimento}'