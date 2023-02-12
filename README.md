# BOFA Transfer Counter

This is a simple script used to count the number of transfers in a Bank of America Account Activity page using regular expressions.
Instructions on how to use it are below.

## Instructions

1. Download bofa_money_counter.py. You can optionally download bofa.txt, which is a sample file that you can use to test the script. If you do not download bofa.txt, you will have to create your own text file called bofa.txt.

2. Navigate to your desired Bank of America account.

3. Click on the "Activity" tab.
![Activity Tab](tutorial_imgs/img1.png)

4. Click on the Filter button on the right. Filter by Tranfers.
![Filter Button](tutorial_imgs/img2.png)

5. (Optional) You can filter by a search term, such as a person's name.
![Search Term](tutorial_imgs/img3.png)

6. Copy the contents of the transactions section.
![Copy Contents](tutorial_imgs/img4.png)

7. Paste contents into a file called bofa.txt. This file must exist in the same directory as the script (bofa_money_counter.py).
![Paste Contents](tutorial_imgs/img5.png)

8. Run the script. Instructions on how to run the script depend on your operating system.

9. Enjoy!

## Usage
For Mac/Linux, open your terminal and run the following command:
    
    python3 bofa_money_counter.py
    
For Windows, open your command prompt and run the following command:
    
    python bofa_money_counter.py


## Notes

* Any file not named bofa.txt will be ignored.
* The script will count all transfers, including those that are processing.
* THIS IS NOT MALWARE. The source code is available for you to see.