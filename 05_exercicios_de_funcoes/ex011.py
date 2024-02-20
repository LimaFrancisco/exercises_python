"""Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. """

def date_in_full(date):
    day = ("1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st","22nd","23th","24th","25th","26th","27th","28th","29th","30th","31st")

    month = "januray","february","march","april","may","juny","july","august","september","october","november","december"