class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        
        compressed_index = 0
        current_char = chars[0]
        current_char_sz = 1
        
        for R in range(1, len(chars)): 
            new_char = chars[R]
            
            if new_char == current_char:
                current_char_sz += 1
            else:
                # Update the compressed list
                chars[compressed_index] = current_char
                
                # Move the compressed_index forward
                compressed_index += 1
                
                if current_char_sz > 1:
                    count_str = str(current_char_sz)
                    for char in count_str:
                        chars[compressed_index] = char
                        compressed_index += 1
                
                current_char = new_char
                current_char_sz = 1
        
        chars[compressed_index] = current_char
        compressed_index += 1
        if current_char_sz > 1:
            count_str = str(current_char_sz)
            for char in count_str:
                chars[compressed_index] = char
                compressed_index += 1
        
        for i in range(len(chars) - compressed_index):
            chars.pop()
        
        return len(chars)