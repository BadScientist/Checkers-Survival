import unittest
import sprint_1_code

class testWeaponClass(unittest.TestCase):
    """Test weapon class."""
    def test_1(self):
        """Test knife weapon randomization"""
        knife_dmg_table = [2,3,4,5,6]
        knife = sprint_1_code.weapon("Knife", "Used for hunting.", 2, 6)
        # run the loop 100 times
        print(knife)
        for num in range(1,101):
            self.assertIn(knife.rand_dmg(), knife_dmg_table)


class testConsumableClass(unittest.TestCase):
    """Test consumable class."""
    def test_1(self):
        """test item use"""
        med_kit = sprint_1_code.consumable("med kit", "Heals a unit by 10. Two uses.", 10, 2) # two uses
        med_kit.use_item() #using item should decrement use count by 1
        self.assertEqual(med_kit.get_use_count(), 1)


if __name__ == '__main__':
    unittest.main(exit=False)
