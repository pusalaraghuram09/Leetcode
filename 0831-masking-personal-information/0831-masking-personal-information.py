class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            # Email
            s = s.lower()
            name, domain = s.split('@')

            return name[0] + "*****" + name[-1] + "@" + domain

        else:
            # Phone number
            digits = ""

            for ch in s:
                if ch.isdigit():
                    digits += ch

            local = "***-***-" + digits[-4:]

            if len(digits) == 10:
                return local

            country_code = "+" + "*" * (len(digits) - 10)

            return country_code + "-" + local