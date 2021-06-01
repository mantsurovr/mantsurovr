# Simple script to generate random examples
import random
import operator


def main():
    # Счетчик количества генерируемых примеров
    x = 0
    while x != 20:
        operands = ['-', '+']
        ops = {
            '+':operator.add,
            '-':operator.sub
        }
        digit1 = random.randint(1, 20)
        digit2 = random.randint(1, 20)
        digit3 = random.randint(1, 20)
        digit4 = random.randint(1, 20)
        operand1 = random.choice(operands)
        operand2 = random.choice(operands)
        operand3 = random.choice(operands)
        sum1 = ops.get(operand1)(digit1, digit2)
        sum2 = ops.get(operand2)(sum1, digit3)
        sum3 = ops.get(operand3)(sum2, digit4)
        if sum1 in range(1, 20) and sum2 in range(1, 20) and sum3 in range(1, 20):
            print(digit1, operand1, digit2, operand2, digit3, operand3, digit4, '=')
            print(sum1, sum2, sum3)
            x += 1

        else:
            continue


if __name__ == '__main__':
    main()

