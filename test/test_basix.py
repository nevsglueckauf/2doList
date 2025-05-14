import unittest
import pandas as pd

class TestBasix(unittest.TestCase):
    """ Unit testing 
            - foo 
            - basix
    """
    def test_basix(self):
        df = pd.DataFrame([[2, 'Peter'], [8, 'Paula']], columns=['id', 'Titel'])
        edited = pd.DataFrame([[2, 'Peter'], [8, 'Zarah']], columns=['id', 'Titel'])
        
        merged_df = pd.merge(df, edited, how='outer', indicator=True)
        found = merged_df[merged_df['_merge'] == 'right_only']
        print(found.iloc[0])
        self.assertTrue(1+1 ==2)
        
        
if __name__ =='__main__':
    unittest.main()
    
 