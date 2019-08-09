#!/usr/bin/python3

#from sys import argv
from optparse import OptionParser
import plotly.graph_objects as go

parser = OptionParser()

parser.add_option('-x', '--xname', dest='xname', help='nome do eixo x', action='store')
parser.add_option('-y', '--yname', dest='yname', help='nome do eixo y', action='store')
parser.add_option('-t', '--title', dest='title', help='título do gráfico', action='store')
parser.add_option('-f', '--transform', dest='transform', help='string de transformação do y', action='store')

(options, argv) = parser.parse_args()

#name = argv[0]

x = []
y = []

fig = go.Figure()
fig.update_layout(
	title=go.layout.Title(
		text=options.title,
		xref='paper',
		x=0
	),
	xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text=options.xname,
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#7f7f7f"
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text=options.yname,
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#7f7f7f"
            )
        )
    )
)

def transform(v, t):
	return eval('{}{}'.format(v, t))

try:
	line = input()
	while True:
		s = [float(x) for x in line.split(';')]
		s[1] = transform(s[1], options.transform)
		y.append(s[1])
		x.append(s[0])
		line = input()
except EOFError:
	pass

fig.add_trace(go.Scatter(x=x, y=y, name='CpuLoad/Time'))
fig.show()
