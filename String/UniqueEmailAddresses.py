"""
Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

 

Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
 

Note:

1 <= emails[i].length <= 100
1 <= emails.length <= 100
Each emails[i] contains exactly one '@' character.


替换 . 和 + 即可。

测试地址：
https://leetcode.com/contest/weekly-contest-108/problems/unique-email-addresses/

"""
import re

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        result = 0
        # local = {}
        _emails = set()
        ignore = re.compile(r'\+(.*)')
        for i in emails:
            x = i.split('@')
            if len(x) > 2:
                continue
            
            if len(x) == 1:
                continue
            
            local = x[0]
            domain = x[1]
            local = local.replace('.', '')

            
            local = re.sub(ignore, '', local)
            
            _emails.add(local + '@' + domain)
        
        return len(_emails)
        