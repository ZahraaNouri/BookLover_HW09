from booklover import BookLover 
import unittest

class BookLoverTestSuite(unittest.TestCase):
   
    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        member = BookLover("Zahra", "Zahra@example.com", "Fantasy")
        member.add_book("Rumi", 5)
        self.assertTrue("Rumi" in member.book_list['book_name'].values)
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        member = BookLover("Zahra", "Zahra@example.com", "Fantasy")
        member.add_book("Rumi", 5)
        member.add_book("Rumi", 5)
        self.assertEqual(len(member.book_list), 1)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        member = BookLover("Zahra", "Zahra@example.com", "Fantasy")
        member.add_book("Rumi", 5)
        self.assertTrue(member.has_read("Rumi"))
    
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        member = BookLover("Zahra", "Zahra@example.com", "Fantasy")
        self.assertFalse(member.has_read("The Ring"))

        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        member = BookLover("Zahra", "Zahra@example.com", "Fantasy")
        member.add_book("Rumi", 5)
        member.add_book("The Ring", 3)
        member.add_book("Harry Potter", 4)
        self.assertEqual(member.num_books_read(), 3)

        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        member = BookLover("Zahra", "Zahra@example.com", "Fantasy")
        member.add_book("Rumi", 5)
        member.add_book("The Ring", 3)
        member.add_book("Harry Potter", 4)
        fav_books = member.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))


        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)