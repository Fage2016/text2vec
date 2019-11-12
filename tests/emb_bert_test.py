# -*- coding: utf-8 -*-
"""
@author:XuMing（xuming624@qq.com)
@description: 
"""
from simtext.embeddings.bert_embedding import BERTEmbedding

if __name__ == '__main__':
    b = BERTEmbedding(model_folder='/Users/xuming06/Codes/bert/data/chinese_L-12_H-768_A-12',
                      sequence_length=12)

    data1 = 'all work and no play makes'.split(' ')
    data2 = '你 好 啊'.split(' ')
    r = b.embed([data1], True)

    tokens = b.process_x_dataset([['语', '言', '模', '型']])[0]
    target_index = [101, 6427, 6241, 3563, 1798, 102]
    target_index = target_index + [0] * (12 - len(target_index))
    assert list(tokens[0]) == list(target_index)
    print(tokens)
    print(r)
    print(r.shape)