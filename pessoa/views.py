from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Pessoa,CadastroDeAluguel
from django.template import loader
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import string


rodape='Praça da Matriz, 145 - Centro - CEP 39550-000 - Taiobeiras/MG'
RODAPE_L_2='Telefone :(38) 3845-1022 - www.taiobeiras.com'
CABE_1='CONTRATO DE COMODATO DE EQUIPAMENTO <br />DE AUXÍLIO AO ENFERMO CARENTE'
paragrafo3='Taiobeiras (MG), %s de %s de %s'
mes_ext = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7:'julho', 8:'agosto', 9:'setembro', 10:'outubro', 11:'novembro', 12:'dezembro'}
TXT_CONTRATO_1="Pelo presente instrumento particular de comodato, de um lado o <b>ROTARY CLUB DE TAIOBEIRAS</b>, MG, Distrito nº 4.520, é uma associação civil sem fins lucrativos, constituída e fundada em 16 de março de 2007, cujos propósitos são de índole humanitária e beneficente, em conformidade com a legislação vigente admitida como membro do <b>ROTARY INTERNATIONAL</b> em 25 de abril de 2007, (Carta de Admissão nº. 75.845), com sede na Rua Bom Jardim, 221 - Centro em Taiobeiras/MG, neste ato representado pelo presidente <b>Dr. João Carlos Sarmento</b>, brasileiro, casado, eng. civil,  Identidade nº. M-1323568SSP/MG e do CPF nº. 489 961 866-91, residente na Avenida da Liberdade, nº 216, Centro, Taiobeiras/MG, de ora em diante chamado simplesmente de <b>COMODANTE</b>, e de outro lado,"
TXT_CONTRATO_2="Nome: <b>%s</b>, 	Estado Civil: <b>%s</b>, Profissão: <b>%s</b>, Nacionalidade: <b>%s</b>,	Identidade:<b>%s</b>, CPF:<b>%s</b>, Endereço: <b>%s</b>, Bairro: <b>%s</b>, Cidade: <b>%s</b>, <b>%s</b>	Contato: <b>%s</b>"
TXT_CONTRATO_3="de ora em diante chamado simplesmente de COMODATÁRIO(a), têm, entre si, como justo e contratado o que se segue:"
TXT_CONTRATO_4=" - O ROTARY CLUB DE TAIOBEIRAS, neste ato denominado de COMODANTE, é proprietário de equipamentos consubstanciados em cadeiras de rodas, andadores, cadeiras de banho, colchões d’água, muletas, comadres, papagaios e outros congêneres, de auxilio ao enfermo carente, identificados com o símbolo do Rotary Club Internacional."
TXT_CONTRATO_5=" - Pelo presente instrumento, o COMODANTE cede em comodato ao COMODATÁRIO(a) acima qualificado, o(s) seguinte(s) equipamento(s):"
TXT_CONTRATO_6="Discriminar o(s) equipamento (s):"
TXT_CONTRATO_7="01(uma) Cadeira de Rodas e 01 cadeira de banho"
TXT_CONTRATO_8="pelo prazo de convalescença do enfermo(a) beneficiado(a), quando não mais necessitará de seu uso, a contar da assinatura do presente contrato, que será(ão) utilizado(s) pelo(a) Sr(a):"
TXT_CONTRATO_9="Nome: <b>%s</b>, Estado Civil: <b>%s</b>, Profissão: <b>%s</b>, Nacionalidade: <b>%s</b>,	Identidade:<b>%s</b>, CPF:<b>%s</b>, Endereço: <b>%s</b>, Bairro: <b>%s</b>, Cidade: <b>%s</b>, <b>%s</b>	Contato: <b>%s</b>"
TXT_CONTRATO_10="o aval do(a) companheiro(a):"
TXT_CONTRATO_11="Nome: %s, Fone: %s"
TXT_CONTRATO_12="<b>3º</b> - O(a) COMODATÁRIO(a) somente poderá destinar o uso do(s) equipamento(s) para o enfermo beneficiário descrito acima, não podendo ceder à outra pessoa, a que título for, sem autorização do COMANDANTE, sob pena de rescisão deste instrumento, dada a necessidade de lavratura de novo contrato."
TXT_CONTRATO_13="<b>4º</b> - O(a) COMODATÁRIO(a) obriga-se a conservar e manter o(s) equipamento(s) emprestado(s) em perfeito estado, promovendo as reparações que se fizerem necessárias e devolvê-lo(s) quando dele(s) não mais necessitar, nas condições acima relatadas, ressalvado o desgaste natural pelo tempo de uso, sob pena de ter que restituir novo(s) equipamento(s) ao COMODANTE, ou responder por perdas e danos a título de indenização."
TXT_CONTRATO_14="<b>5º</b> - O(a) COMANDATÁRIO(a) não poderá alterar, no todo ou em parte, o(s) equipamento(s) que ora lhe é(são) cedido(s), sendo de sua responsabilidade todas as despesas e reparos decorrentes de sua(s) utilização(ões) pelo enfermo beneficiado."
TXT_CONTRATO_15="<b>6º</b> - O(a) COMODATÁRIO(a) que não devolver o(s) equipamento(s) quando solicitado(s) pelo COMANDANTE, ou quando dele(s) o enfermo beneficiado não mais necessitar, pagará o aluguel durante o tempo de atraso em restituí-lo(s), no valor de 20% do salário mínimo mensal, ou responder por perdas e danos."
TXT_CONTRATO_16="<b>7º</b> -  Fica eleito o Foro da Comarca de Taiobeiras/MG, com exclusão de qualquer outro, por mais privilegiado que seja, para dirimir quaisquer dúvidas que possam surgir na execução do presente contrato."
TXT_CONTRATO_17="<b>8º</b> - Poderá o enfermo beneficiado assinar o contrato de comodato como contratado, caso sua saúde não o impede de assumir o cumprimento das cláusulas contratuais."
TXT_CONTRATO_18="E por estarem assim justos e contratados, assinam e ratificam o presente contrato em duas vias de igual teor e forma, na presença das testemunhas, abaixo-assinadas."
TXT_CONTRATO_19='Taiobeiras (MG), %s de %s de %s<br /><br />'
#TXT_CONTRATO_19="Taiobeiras/MG, 05 de novembro de 2015."
TXT_CONTRATO_20="_______________________________________<br />"
TXT_CONTRATO_21="<b>Rotary Club de Taiobeiras</b>"
TXT_CONTRATO_22="<b>Comodante</b><br /><br /><br />"
TXT_CONTRATO_23="_______________________________________<br />"
TXT_CONTRATO_24="Comodatário(a)<br /><br />"
TXT_CONTRATO_25="Testemunhas:<br />"
TXT_CONTRATO_26="_________________________________________________<br />"
TXT_CONTRATO_27="_________________________________________________<br />"


def index(request):
    latest_question_list = Pessoa.objects.order_by('-nome')
    template = loader.get_template('pessoa/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, pessoa_id):
    try:
        pessoa = Pessoa.objects.get(pk=contribuinte_id)
    except Pessoa.DoesNotExist:
        raise Http404("Pessoa Não Existe")
    return render(request, 'éssoa/detail.html', {'pessoa': pessoa})

def gerarcontrato(request,cadastrodealuguel_id):
    from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
    from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate
    from reportlab.lib.units import inch
    from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
    from datetime import date
    from PIL import Image

    obito = CadastroDeAluguel.objects.get(pk=cadastrodealuguel_id)
    hj =date.today()
    texttext=TXT_CONTRATO_19 %(hj.day,mes_ext[hj.month],hj.year)
    def pegadados(parag):
        aluguel = CadastroDeAluguel.objects.get(pk=cadastrodealuguel_id)
        falecido=aluguel.comodante.nome


        s = parag %(aluguel.comodante.nome,aluguel.comodante.etadocivil,aluguel.comodante.profissao,aluguel.comodante.nacionalidade,aluguel.comodante.rg,aluguel.comodante.cpf,aluguel.comodante.endereco,aluguel.comodante.bairro,aluguel.comodante.municipios,aluguel.comodante.numero,aluguel.comodante.telefone,)
        return s

    def pegadados2(parag):
        aluguel = CadastroDeAluguel.objects.get(pk=cadastrodealuguel_id)

        s = parag %(aluguel.usuario.nome,aluguel.usuario.etadocivil,aluguel.usuario.profissao,aluguel.usuario.nacionalidade,aluguel.usuario.rg,aluguel.usuario.cpf,aluguel.usuario.endereco,aluguel.usuario.bairro,aluguel.usuario.municipios,aluguel.usuario.numero,aluguel.usuario.telefone,)
        return s
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="termodeciencia.pdf"'


    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', font='Times-Roman', alignment=TA_JUSTIFY,fontSize=11,firstLineIndent=25,leading=20))
    styles.add(ParagraphStyle(name='Titulo', font='Times-Roman',alignment=TA_CENTER,fontSize=14))
    styles.add(ParagraphStyle(name='Titulo2', font='Times-Roman',alignment=TA_CENTER,fontSize=12))

    styles.add(ParagraphStyle(name='assinatura', font='Times-Roman',alignment=TA_CENTER,fontSize=12))

    Elements=[]
    """Rodapé da pagina"""
##    '''showBoundary=1''' isso ativa as bordas do texto
    doc = BaseDocTemplate(response,showBoundary=0)


    def foot1(canvas,doc):
        """Rodapé da pagina"""
        canvas.saveState()
        canvas.setFont('Times-Roman',12)
        #canvas.drawImage('contribuinte/static/logo/brasao.jpg',250, 725)
##        canvas.drawString(1.50 * inch, 2.75 * inch, TERMO_DE_CIENCIA_P_3)
        canvas.drawString(1.70 * inch, 0.75 * inch, rodape)
        canvas.drawString(2.05 * inch, 0.60 * inch, RODAPE_L_2)
        canvas.restoreState()
    def foot2(canvas,doc):
        canvas.saveState()
        canvas.setFont('Times-Roman',12)

        canvas.drawString(2.70 * inch, 0.75 * inch, "Page %d" % doc.page)
        canvas.restoreState()

    frameT = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='Justify')
    Elements.append(Paragraph('<h1><b>'+CABE_1+'</b></h1><br /><br />',styles['Titulo2']))
    Elements.append(Paragraph('<br />',styles['Justify']))
    Elements.append(Paragraph('',styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_1,styles['Justify']))

    Elements.append(Paragraph('<br />',styles['Justify']))
    Elements.append(Paragraph(pegadados(TXT_CONTRATO_2),styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_3,styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_4,styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_5,styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_6,styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_7,styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_8,styles['Justify']))
    Elements.append(Paragraph(pegadados2(TXT_CONTRATO_9),styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_10,styles['Justify']))
    #Elements.append(Paragraph(pegadados(TXT_CONTRATO_11),styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_12,styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_13,styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_14,styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_15,styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_16,styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_17,styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_18,styles['Justify']))
    Elements.append(Paragraph(texttext,styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_20,styles['assinatura']))
    Elements.append(Paragraph(TXT_CONTRATO_21,styles['assinatura']))
    Elements.append(Paragraph(TXT_CONTRATO_22,styles['assinatura']))
    Elements.append(Paragraph(TXT_CONTRATO_23,styles['assinatura']))
    Elements.append(Paragraph(TXT_CONTRATO_24,styles['assinatura']))
    Elements.append(Paragraph(TXT_CONTRATO_25,styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_26,styles['Justify']))
    Elements.append(Paragraph(TXT_CONTRATO_27,styles['Justify']))


    #Elements.append(Paragraph(TERMO_DE_CIENCIA_P_2 %(obito.cemiterio,obito.falecido.nome),styles['Justify']))

    #Elements.append(Paragraph(TERMO_DE_CIENCIA_P_3,styles['Justify']))
    Elements.append(PageBreak())
    doc.addPageTemplates([PageTemplate(id='OneCol',frames=frameT,onPage=foot1),])
    doc.build(Elements)
    response.write(doc)
    return response