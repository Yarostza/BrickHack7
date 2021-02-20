#pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
import twint

c = twint.Config()

c.Username = "barackobama"
c.Limit = 10
c.Store_csv = False
c.Output = "none"

twint.run.Search(c)