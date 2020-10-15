import torch
import torch.nn as nn 
from transformers import XLNetConfig, XLNetForSequenceClassification

class Model(nn.Module):
    def __init__(self, config):
        super(Model, self).__init__()
        model_config = XLNetConfig.from_pretrained(config.bert_path, num_labels=config.num_classes)
        self.xlnet = XLNetForSequenceClassification(config.bert_path, config=model_config)
        for param in self.xlnet.parameters():
            param.requires_grad = True
        self.fc = nn.Linear(config.hidden_size, config.num_classes)
    
    def forward(self, x):
        context, mask, token_type_ids = x[0], x[1], x[2]
        _, pooled = self.xlnet(context, attention_mask=mask, token_type_ids=token_type_ids)
        out = self.fc(pooled)
        return out 
