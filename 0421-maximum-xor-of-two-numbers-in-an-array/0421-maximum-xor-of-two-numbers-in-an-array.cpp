#include <iostream>
#include <vector>

using namespace std;

class TrieNode {
public:
    TrieNode() {
        kids = vector<TrieNode*>(2, nullptr);
        isEnd = false;
    }
    
    vector<TrieNode*> kids;
    bool isEnd;
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string bit) {
        TrieNode* cur = root;
        
        for (char c : bit) {
            int bit_val = c - '0';
            if (cur->kids[bit_val] == nullptr) {
                cur->kids[bit_val] = new TrieNode();
            }
            
            cur = cur->kids[bit_val];
        }
        
        cur->isEnd = true;
    }
    
    int max_val(string bit) {
        TrieNode* cur = root;
        int res = 0;
        
        for (char c : bit) {
            int bit_val = c - '0';
            int flip_bit = 1 - bit_val; // Flip the bit
            if (cur->kids[flip_bit] != nullptr) {
                res = (res << 1) | 1; // Append 1 to the result
                cur = cur->kids[flip_bit];
            } else {
                res = (res << 1); // Append 0 to the result
                cur = cur->kids[bit_val];
            }
        }
        
        return res;
    }
    
private:
    TrieNode* root;
};

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        Trie trie;
        int max_val = 0;
        int mask = 0;
        
        for (int i = 31; i >= 0; i--) {
            mask = mask | (1 << i);
            unordered_set<int> prefixes;
            
            for (int num : nums) {
                prefixes.insert(num & mask);
            }
            
            int temp_max = max_val | (1 << i);
            
            for (int prefix : prefixes) {
                int complement = prefix ^ temp_max;
                if (prefixes.count(complement)) {
                    max_val = temp_max;
                    break;
                }
            }
        }
        
        return max_val;
    }
};
