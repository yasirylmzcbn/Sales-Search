import sqlite3

class Search:
    
    def department_total(self, dept):
        conn = sqlite3.connect('sales.sqlite')
        cursor = conn.execute("SELECT sum(amount) FROM sales where department = '" + dept + "'")
        sum = 0
        for i in cursor:
            sum = i[0]
            break
        return sum

    def department_total_bydate(self, dept, date):
        conn = sqlite3.connect('sales.sqlite')
        cursor = conn.execute("SELECT SUM(amount) FROM sales where department = '"+dept+"' and sale_date = '"+date+"'")
        for i in cursor:
            return i[0]
        return None

    def country_count_date_range(self, country, start_date, end_date):
        conn = sqlite3.connect('sales.sqlite')
        cursor = conn.execute("SELECT sum(amount) from sales s join buyers b on s.buyer_id = b.id where country = '"+country+"' and sale_date >= '"+start_date+"' and sale_date <= '"+end_date+"'")
        for i in cursor:
            return i[0]
        return None
    
    def biggest_spender(self):
        conn = sqlite3.connect('sales.sqlite')
        cursor = conn.execute("SELECT buyer_id, sum(amount) FROM sales s join buyers b on s.buyer_id group by buyer_id order by sum(amount) DESC limit 1")
        for i in cursor:
            cursor2 = conn.execute("SELECT first_name, last_name from buyers where id = '"+str(i[0])+"'")
            break
        for j in cursor2:
            tup = (j[0],j[1])
        return tup
    def biggest_spenders(self, how_many, department):
        conn = sqlite3.connect('sales.sqlite')
        cursor = conn.execute("SELECT first_name, last_name, buyer_id, sum(amount) FROM sales s join buyers b on s.buyer_id = b.id where department = '"+department+"' group by buyer_id ORDER BY sum(amount) DESC, first_name ASC, last_name limit "+str(how_many))
        lst = []
        amount = 0.
        for i in cursor:
            amount = float(i[3]/1000)
            i = (list(i))
            i.pop(2)
            i = tuple(i)
            lst.append(i)
        return lst