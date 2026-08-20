class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = {}

        for card in hand:
            count[card] = count.get(card, 0) + 1

        hand.sort()

        for card in hand:
            if count[card] == 0:
                continue

            for x in range(card, card + groupSize):
                if count.get(x, 0) == 0:
                    return False

                count[x] -= 1

        return True