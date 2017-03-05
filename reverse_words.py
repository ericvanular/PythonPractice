
def reverse_words(message):
    message_chars = list(message)
    message_len = len(message)
    for i in range(len(message_chars)/2):
        temp = message_chars[i]
        message_chars[i] = message_chars[message_len - i - 1]
        message_chars[message_len - i - 1] = temp
        
        
    start_idx = 0
    for end_idx in range(len(message_chars) + 1):
        if end_idx == len(message_chars) or message_chars[end_idx] == ' ':
            word_mid_idx = start_idx + (end_idx - start_idx)/2     
            offset = 0
            for i in range(start_idx, word_mid_idx):
                temp = message_chars[i]
                message_chars[i] = message_chars[end_idx - offset - 1]
                message_chars[end_idx - offset - 1] = temp
                offset += 1
            start_idx = end_idx + 1
                         
    
                         
        
            
        
    
    return ''.join(message_chars)

message = 'find you will pain only go you recordings security the into if'

print reverse_words(message)