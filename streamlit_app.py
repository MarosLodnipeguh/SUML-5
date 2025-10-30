import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
# zaczynamy od zaimportowania bibliotek
from transformers import pipeline

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')
# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.

# Inne przykłady do wypróbowania:
# st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

# st.spinner()
# with st.spinner(text='Pracuję...'):
    # time.sleep(2)
    # st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

# główny tytuł aplikacji (dostosuj do swoich potrzeb)
st.title('Tłumacz EN → DE i analiza sentymentu — Lab05')
# title, jak sama nazwa wskazuje, używamy do wyświetlenia tytułu naszej aplikacji

# st.header('Wprowadzenie do zajęć')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

# st.subheader('O Streamlit')
# subheader to jeden z podtytułów wykorzystywnaych w Streamlit

# st.text('To przykładowa aplikacja z wykorzystaniem Streamlit')
# text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.

# st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')
# write używamy również do wyświetlenia tekstu, różnica polega na formatowaniu.

# st.code("st.write()", language='python')
# code może nam się czasami przydać, jeżeli chcielibyśmy pokazać np. klientowi fragment kodu, który wykorzystujemy w aplikacji

# with st.echo():
#     st.write("Echo")
# możemy też to zrobić prościej używając echo - pokazujemy kod i równocześnie go wykonujemy

# df = pd.read_csv("DSP_4.csv", sep = ';')
# st.dataframe(df)
# musimy tylko pamiętać o właściwym określeniu separatora (w tym wypadku to średnik)
# masz problem z otworzeniem pliku? sprawdź w jakim katalogu pracujesz i dodaj tam plik (albo co bardziej korzystne - zmień katalog pracy)
# os.getcwd() # pokaż bieżący katalog
# os.chdir("") # zmiana katalogu

st.header('Przetwarzanie języka naturalnego')

option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tłumaczenie tekstu (en -> de)",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        with st.spinner('Analizuję sentyment...'):
            try:
                classifier = pipeline("sentiment-analysis")
                answer = classifier(text)
                st.success('Analiza zakończona')
                st.write(answer)
            except Exception as e:
                st.error(f'Wystąpił błąd podczas analizy: {e}')

elif option == "Tłumaczenie tekstu (en - de)":
    text = st.text_area(label="Wpisz tekst po ang")
    if text:
        with st.spinner('Tłumacze tekst'):
            try:
                translator = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")
                result = translator(text, max_length=400)
                translation = result[0].get('translation_text') if isinstance(result, list) else result
                st.success('Tłumaczenie gotowe')
                st.write(translation)
            except Exception as e:
                st.error(f'Błąd: {e}')

st.title('s28781')

st.subheader('Zadanie do wykonania')
st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/docs/transformers/index')
st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')
