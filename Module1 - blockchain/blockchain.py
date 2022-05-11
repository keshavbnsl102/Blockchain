#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 23:14:03 2022

@author: keshavbansal
"""

import datetime
import hashlib
import json 
from flask import Flask,jsonify

print(2)

class Blockchain:
    
    def __init__(self):
        self.chain=[]
        self.create_block(proof=1,previous_hash='0')
        
    def create_block(self, proof , previous_hash):
        block={'index': len(self.chain)+1,
               'timestamp': str(datetime.datetime.now()),
               'proof': proof,
               'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof=1
        check_proof=False
        while check_proof is False:
            hash_operation= hashlib(str(new_proof**2-old_proof**2).encode()).hexdigest()
            if hash_operation[:4]=='0000':
                check_proof=True
            else:
                new_proof+=1
        return new_proof
            
            
    
    
    
        
