class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        lines = []
        current_line = []
        current_width = 0

        for word in words:
            if current_width + len(word) + len(current_line) > maxWidth:
                lines.append(current_line)
                current_line = []
                current_width = 0
            current_line.append(word)
            current_width += len(word)
        
        if current_line:
            lines.append(current_line)

        justified_text = []
        for i, line in enumerate(lines):
            if i == len(lines) - 1 or len(line) == 1:
                justified_text.append(' '.join(line).ljust(maxWidth))
            else:
                total_spaces = maxWidth - sum(len(word) for word in line)
                space_between_words, extra_spaces = divmod(total_spaces, len(line) - 1)
                for j in range(extra_spaces):
                    line[j] += ' '
                justified_text.append((' ' * space_between_words).join(line))
        return justified_text
