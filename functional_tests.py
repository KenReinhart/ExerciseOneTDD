from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    #open the browser
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    #test everything 
    def test_can_start_a_list_and_retrieve_it_later(self):
        #checking out the homepage
        self.browser.get('http://localhost:8000')
    
    #then close the browser, this will be a cue for us that the testing is finished
    def tearDown(self):
        self.browser.quit()
        
if __name__ == '__main__':
    unittest.main()