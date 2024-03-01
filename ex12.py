att, comp, yds, td, int_ = map(float, input().split())
c = ((comp/att)*100-30)/20
y = (yds/att-3)*(1/4)
t = (td/att)*20
i = 2.375-((int_/att)*25)
passer_rating = ((max(min(c, 2.375), 0) + max(min(y, 2.375), 0) + max(min(t, 2.375), 0) + max(min(i, 2.375), 0))/3)*50
print(passer_rating)
