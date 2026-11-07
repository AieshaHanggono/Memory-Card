from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import *

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = list()
questions_list.append(Question('Negara dengan populasi terbanyak di dunia?', 'India', 'China', 'Amerika Serikat', 'Indonesia'))
questions_list.append(Question('Sungai terpanjang di dunia?', 'Sungai Nil', 'Sungai Amazon', 'Sungai Yangtze', 'Sungai Mississippi'))
questions_list.append(Question('Danau terbesar di dunia (berdasarkan luas permukaan)?', 'Laut Kaspia', 'Danau Superior', 'Danau Victoria', 'Danau Baikal'))
questions_list.append(Question('Gurun terluas di dunia (selain Antartika)?', 'Gurun Sahara', 'Gurun Gobi', 'Gurun Arab', 'Gurun Kalahari'))
questions_list.append(Question('Samudra terluas di dunia?', 'Samudra Pasifik', 'Samudra Atlantik', 'Samudra Hindia', 'Samudra Arktik'))
questions_list.append(Question('Negara terluas di dunia berdasarkan wilayah?', 'Rusia', 'Kanada', 'China', 'Amerika Serikat'))
questions_list.append(Question('Gunung tertinggi di dunia?', 'Gunung Everest', 'K2', 'Gunung Kilimanjaro', 'Gunung McKinley'))
questions_list.append(Question('Ibukota dari negara Australia?', 'Canberra', 'Sydney', 'Melbourne', 'Brisbane'))
questions_list.append(Question('Negara yang mendapat julukan Negeri Matahari Terbit?', 'Jepang', 'Korea Selatan', 'China', 'Thailand'))
questions_list.append(Question('Selat yang memisahkan Pulau Jawa dan Pulau Sumatera?', 'Selat Sunda', 'Selat Malaka', 'Selat Bali', 'Selat Madura'))
questions_list.append(Question('Air terjun tertinggi di dunia?', 'Angel Falls', 'Niagara Falls', 'Victoria Falls', 'Iguazu Falls'))
questions_list.append(Question('Negara terkecil di dunia berdasarkan luas wilayah?', 'Vatikan', 'Monako', 'Nauru', 'Tuvalu'))
questions_list.append(Question('Pegunungan terpanjang di dunia yang berada di Amerika Selatan?', 'Pegunungan Andes', 'Pegunungan Himalaya', 'Pegunungan Rocky', 'Pegunungan Alpen'))
questions_list.append(Question('Ibukota dari negara Prancis?', 'Paris', 'Lyon', 'Marseille', 'Nice'))
questions_list.append(Question('Negara yang dikenal dengan sebutan Negeri Kincir Angin?', 'Belanda', 'Jerman', 'Inggris', 'Denmark'))
questions_list.append(Question('Laut terdalam di dunia?', 'Palung Mariana', 'Palung Puerto Riko', 'Palung Jawa', 'Palung Tonga'))
questions_list.append(Question('Benua terkecil di dunia?', 'Australia', 'Eropa', 'Antartika', 'Amerika Selatan'))
questions_list.append(Question('Kanal buatan manusia yang menghubungkan Laut Mediterania dan Laut Merah?', 'Kanal Suez', 'Kanal Panama', 'Kanal Kiel', 'Kanal Korintus'))
questions_list.append(Question('Negara kepulauan terbesar di dunia?', 'Indonesia', 'Filipina', 'Jepang', 'Madagaskar'))
questions_list.append(Question('Garis khayal yang membagi bumi menjadi belahan utara dan selatan?', 'Garis Khatulistiwa', 'Garis Meridian', 'Garis Balik Utara', 'Garis Balik Selatan'))
questions_list.append(Question('Negara yang terletak di dua benua sekaligus (Asia dan Eropa)?', 'Turki', 'Mesir', 'Yunani', 'Ukraina'))
questions_list.append(Question('Ibukota dari negara Jepang?', 'Tokyo', 'Kyoto', 'Osaka', 'Hiroshima'))
questions_list.append(Question('Pulau terbesar di dunia (bukan benua)?', 'Greenland', 'Sini', 'Kalimantan', 'Madagaskar'))
questions_list.append(Question('Gurun pasir terluas di benua Asia?', 'Gurun Gobi', 'Gurun Arab', 'Gurun Thar', 'Gurun Karakum'))
questions_list.append(Question('Negara yang mengelilingi seluruh wilayah negara kecil Vatikan?', 'Italia', 'Prancis', 'Spanyol', 'Swiss'))
questions_list.append(Question('Laut yang memisahkan benua Asia dan benua Afrika?', 'Laut Merah', 'Laut Hitam', 'Laut Kaspia', 'Laut Mediterania'))
questions_list.append(Question('Kota di Amerika Serikat yang mendapat julukan "The Big Apple"?', 'New York', 'Los Angeles', 'Chicago', 'Miami'))
questions_list.append(Question('Pegunungan tertinggi di benua Eropa?', 'Pegunungan Alpen', 'Pegunungan Andes', 'Pegunungan Ural', 'Pegunungan Rocky'))
questions_list.append(Question('Negara yang memiliki garis pantai terpanjang di dunia?', 'Kanada', 'Indonesia', 'Australia', 'Rusia'))
questions_list.append(Question('Negara yang terkenal dengan julukan "Negeri Tirai Bambu"?', 'China', 'Jepang', 'Korea Utara', 'Vietnam'))
questions_list.append(Question('Ibukota dari negara Inggris (United Kingdom)?', 'London', 'Edinburgh', 'Manchester', 'Liverpool'))
questions_list.append(Question('Selat yang memisahkan benua Asia (Rusia) dan benua Amerika (Alaska)?', 'Selat Bering', 'Selat Gibraltar', 'Selat Malaka', 'Selat Magellan'))
questions_list.append(Question('Negara dengan jumlah pulau terbanyak di dunia?', 'Swedia', 'Indonesia', 'Kanada', 'Filipina'))
questions_list.append(Question('Kota paling padat penduduknya di dunia?', 'Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo'))
questions_list.append(Question('Negara berbentuk sepatu bot di benua Eropa?', 'Italia', 'Spanyol', 'Yunani', 'Portugal'))
questions_list.append(Question('Danau terdalam di dunia yang terletak di Siberia?', 'Danau Baikal', 'Danau Tanganyika', 'Danau Caspian', 'Danau Superior'))
questions_list.append(Question('Negara yang memiliki jumlah zona waktu terbanyak di dunia?', 'Prancis', 'Rusia', 'Amerika Serikat', 'Inggris'))
questions_list.append(Question('Laut terkecil dan terdangkal di dunia?', 'Laut Azov', 'Laut Merah', 'Laut Baltik', 'Laut Hitam'))
questions_list.append(Question('Benua yang juga merupakan sebuah negara tunggal?', 'Australia', 'Antartika', 'Afrika', 'Eropa'))
questions_list.append(Question('Negara yang memiliki piramida kuno Giza?', 'Mesir', 'Meksiko', 'Peru', 'Iran'))
questions_list.append(Question('Ibukota dari negara Jerman?', 'Berlin', 'Munchen', 'Frankfurt', 'Hamburg'))
questions_list.append(Question('Semenanjung terbesar di dunia?', 'Semenanjung Arab', 'Semenanjung India', 'Semenanjung Korea', 'Semenanjung Indochina'))
questions_list.append(Question('Negara yang terkenal dengan hewan endemik Kanguru?', 'Australia', 'Selandia Baru', 'Papua Nugini', 'Afrika Selatan'))
questions_list.append(Question('Teluk terbesar di dunia berdasarkan luas wilayah?', 'Teluk Benggala', 'Teluk Meksiko', 'Teluk Persia', 'Teluk Hudson'))
questions_list.append(Question('Negara yang wilayahnya terletak paling selatan di dunia (tidak termasuk Antartika)?', 'Chili', 'Argentina', 'Afrika Selatan', 'Selandia Baru'))
questions_list.append(Question('Ibukota dari negara Korea Selatan?', 'Seoul', 'Busan', 'Incheon', 'Jeju'))
questions_list.append(Question('Pegunungan yang menjadi batas alam antara benua Eropa dan Asia?', 'Pegunungan Ural', 'Pegunungan Alpen', 'Pegunungan Kaukasus', 'Pegunungan Himalaya'))
questions_list.append(Question('Negara yang terkenal dengan sebutan "Negeri Gajah Putih"?', 'Thailand', 'Vietnam', 'Kamboja', 'Myanmar'))
questions_list.append(Question('Samudra terkecil di dunia?', 'Samudra Arktik', 'Samudra Hindia', 'Samudra Pasifik', 'Samudra Atlantik'))


app = QApplication([])
btn_OK = QPushButton('Answer') 
lb_Question = QLabel('The most difficult question in the world!')
RadioGroupBox = QGroupBox("Answer options") 
rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 

RadioGroupBox.setLayout(layout_ans1) 
AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel('are you correct or not?')
lb_Correct = QLabel('the answer will be here!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    ''' show answer panel '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')

def show_question():
    ''' show question panel '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

# Variabel global penampung jawaban benar yang sedang aktif
current_right_answer = ""

def ask(q: Question):
    global current_right_answer
    current_right_answer = q.right_answer # Simpan jawaban benar yang asli
    
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    # Cari tombol mana yang sedang dicentang oleh user
    selected_button = RadioGroup.checkedButton()
    
    if selected_button is not None:
        # Bandingkan teks tombol yang dicentang dengan jawaban benar yang asli
        if selected_button.text() == current_right_answer:
            window.score += 1
            show_correct('Correct!')
        else:
            show_correct('Incorrect!')
        
        # Proteksi pembagian dengan nol menggunakan try-except
        try:
            rating = (window.score / window.total) * 100
        except ZeroDivisionError:
            rating = 0.0
            
        print("Statistic\n-Total Question:", window.total, '\n-Right answers:', window.score)
        print('Rating:', rating, '%')
    else:
        print("Pilih salah satu jawaban terlebih dahulu!")

def next_question():
    window.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_ok():
    if btn_OK.text() == 'Answer':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

window.score = 0
window.total = 0
btn_OK.clicked.connect(click_ok) 
next_question()

window.show()
app.exec()

