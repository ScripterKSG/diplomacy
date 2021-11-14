from io import StringIO
from unittest import main, TestCase

from Diplomacy import diplomacy_read, diplomacy_eval, diplomacy_print, diplomacy_solve

class TestDiplomacy (TestCase):
    # ----
    # read
    # ----
    def test_read_1(self):
        s = "A Houston Move Austin"
        temp = diplomacy_read(s)
        self.assertEqual(temp.name, "A")
        self.assertEqual(temp.location, 'Houston')
        self.assertEqual(temp.action, "Move")
        self.assertEqual(temp.target_loc, 'Austin')
    
    def test_read_2(self):
        s = "B Austin Hold"
        temp = diplomacy_read(s)
        self.assertEqual(temp.name, "B")
        self.assertEqual(temp.location, 'Austin')
        self.assertEqual(temp.action, "Hold")
        self.assertEqual(temp.target_loc, None)

    def test_read_3(self):
        s = "C Dallas Support B"     
        temp = diplomacy_read(s)
        self.assertEqual(temp.name, "C")
        self.assertEqual(temp.location, 'Dallas')
        self.assertEqual(temp.action, "Support")
        self.assertEqual(temp.target_army, "B")

    def test_solve_1(self):
        r = StringIO("A Houston Move Austin\nB Austin Hold\n")
        w = StringIO()

        diplomacy_solve(r,w)
        self.assertEqual("A [dead]\nB [dead]\n", w.getvalue())

    def test_solve_2(self):
        r = StringIO("A Houston Hold\n\
                      B Austin Support C\n\
                      C Dallas Move Houston\n")
        w = StringIO()
        diplomacy_solve(r,w)
        self.assertEqual("A [dead]\nB Austin\nC Houston\n", w.getvalue())

    def test_solve_3(self):
        r = StringIO("A Madrid Hold\n\
                    B Barcelona Move Madrid\n\
                    C London Move Madrid\n\
                    D Paris Support B")
        w = StringIO()
        diplomacy_solve(r,w)
        self.assertEqual("A [dead]\nB Madrid\nC [dead]\nD Paris\n", w.getvalue())
        
    def test_solve_4(self):
        r = StringIO("A Madrid Hold\n\
            B Barcelona Move Madrid\n\
            C London Move Madrid\n\
            D Paris Support B\n\
            E Dublin support D")
        w = StringIO()
        diplomacy_solve(r,w)
        self.assertEqual("A [dead]\nB Madrid\nC [dead]\nD Paris\nE Dublin\n", w.getvalue())
    
    def test_solve_5 (self):
        r = StringIO("A Madrid Hold\n\
            B Barcelona Move Madrid\n\
            C London Move Madrid\n\
            D Paris Support B\n\
            E Dublin support D\n\
                F Dallas move Paris")
        w = StringIO()
        diplomacy_solve(r,w)
        self.assertEqual("A [dead]\nB [dead]\nC [dead]\nD Paris\nE Dublin\nF [dead]\n", w.getvalue())
        
# ----
# main
# ----


if __name__ == "__main__":
    main()
