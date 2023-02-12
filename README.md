# BOFA Transfer Counter

This is a simple script used to count the number of transfers in a Bank of America Account Activity page using regular expressions.
Instructions on how to use it are below.

## Instructions

1. Navigate to your desired Bank of America account.

2. Click on the "Activity" tab.
![Activity Tab](tutorial_imgs/img1.png)

3. Click on the Filter button on the right. Filter by Tranfers.
![Filter Button](tutorial_imgs/img2.png)

4. (Optional) You can filter by a search term, such as a person's name.
![Search Term](tutorial_imgs/img3.png)

5. Copy the contents of the transactions section.
![Copy Contents](tutorial_imgs/img4.png)

6. Paste contents into a file called bofa.txt. This file must exist in the same directory as the script (bofa_money_counter.py).
![Paste Contents](tutorial_imgs/img5.png)

7. Run the script. Instructions on how to run the script depend on your operating system.

8. Enjoy!

## Usage
For Mac/Linux, open your terminal and run the following command:
    
    python3 bofa_money_counter.py
    
For Windows, open your command prompt and run the following command:
    
    python bofa_money_counter.py


## Notes

* Any file not named bofa.txt will be ignored.
* The script will count all transfers, including those that are processing.
* THIS IS NOT MALWARE. The source code is available for you to see.