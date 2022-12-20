import unittest
from unittest import main
from main import b1, b2, b3, one_to_many,many_to_many


class test1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(b1(one_to_many),
                         {'Ату их, ату!': 'Сочинения Джека Лондона'}
                         )

    def test_2(self):
        self.assertEqual(
            b2(one_to_many),[('Спутник работника света', 60), ('Введение в анализ', 41), ('Сочинения Джека Лондона', 19)])

    def test_3(self):
        self.assertEqual(
            b3(many_to_many),[('Ату их, ату!', 322, 'Сочинения Джека Лондона'), ('Белое Безмолвие', 19, 'Сочинения Джека Лондона'),
                ('Воплощение, или инкарнация', 60, 'Спутник работника света'),
                ('Отображение множеств', 70, 'Введение в анализ'),
                ('Сын Волка', 29, 'Сочинения Джека Лондона'), ('Элементы теории множеств', 41, 'Введение в анализ')]
               )


if __name__ == '__main__':
    main()