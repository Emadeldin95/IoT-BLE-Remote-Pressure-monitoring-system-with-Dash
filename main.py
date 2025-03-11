# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
import dash
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input , Output
import dash_core_components as dcc
import plotly.offline  as pyo
import plotly.graph_objs as go
from datetime import datetime
from collections import deque
#import dash_auth
import openpyxl
from openpyxl import load_workbook
idle=1
cycle_running=2
cycle_finished=3
system_state=idle
counter=0

pr1=0
pr2=0
pr3=0
pr4=0
pr5=0
pr6=0
pr7=0
x=deque(maxlen=350)
x.append(0)
y1 = deque(maxlen=350)
y1.append(0)
y2 = deque(maxlen=350)
y2.append(0)
y3 = deque(maxlen=350)
y3.append(0)
y4 = deque(maxlen=350)
y4.append(0)
y5 = deque(maxlen=350)
y5.append(0)
y6 = deque(maxlen=350)
y6.append(0)
y7 = deque(maxlen=350)
y7.append(0)

app=dash.Dash(__name__,   meta_tags=[{'name': 'viewport',
                          'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.8'}]
    )
p=0

#USERNAME_PASSWORD_PAIRS=[['mazen','pass']]
#auth=dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)

gauge1_header=html.H1('Shaping Pressure (Bar)',id='h1',style=dict(color='white'))
gauge1_header_div=html.Div([gauge1_header], style=dict( textAlign='center',fontSize=14,marginTop='-70px'))
gauge1= daq.Gauge( showCurrentValue=False, units="BAR",  id='my-gauge',
        label=dict(label='{}'.format(p),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px')),
        labelPosition='bottom', min=0,max=7, value=p ,  color= '#42C4F7',size=270, style=dict(fontSize=28)
    )
gauge1_div=html.Div([gauge1_header_div,gauge1] ,style=dict(display='inline-block',backgroundColor='#082255' , height='330px'
                                                           ,marginLeft='150px',marginTop='70px' ) )

gauge2_header=html.H1('Sensor 1 Pressure (Bar)',id='h2',style=dict(color='white'))
gauge2_header_div=html.Div([gauge2_header], style=dict( textAlign='center',fontSize=14,marginTop='-70px'))
gauge2= daq.Gauge( showCurrentValue=False, units="BAR",   id='my-gauge2',
        label=dict(label='{}'.format(p),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px')),
        labelPosition='bottom', value=p ,min=0,max=7, color= "#42C4F7",  size=270
    )
gauge2_div=html.Div([gauge2_header_div,gauge2] ,style=dict(display='inline-block',backgroundColor='#082255' , height='330px'
                                                           ,marginLeft='100px',marginTop='40px' ) )

gauge3_header=html.H1('Sensor 2 Pressure (Bar)',id='h3',style=dict(color='white'))
gauge3_header_div=html.Div([gauge3_header], style=dict( textAlign='center',fontSize=14,marginTop='-70px'))
gauge3= daq.Gauge( showCurrentValue=False,units="BAR",  id='my-gauge3',
        label=dict(label='{}'.format(p),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px')),
        labelPosition='bottom', value=p ,min=0,max=7, color= "#42C4F7", size=270
    )
gauge3_div=html.Div([gauge3_header_div,gauge3] ,style=dict(display='inline-block',backgroundColor='#082255' , height='330px'
                                                           ,marginLeft='100px',marginTop='40px' ) )

gauge4_header=html.H1('Sensor 3 Pressure (Bar)',id='h4',style=dict(color='white'))
gauge4_header_div=html.Div([gauge4_header], style=dict( textAlign='center',fontSize=14,marginTop='-70px'))
gauge4= daq.Gauge( showCurrentValue=False,units="BAR",  id='my-gauge4',
        label=dict(label='{}'.format(p),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px')),
        labelPosition='bottom', value=p ,min=0,max=7, color= "#42C4F7", size=270
    )
gauge4_div=html.Div([gauge4_header_div,gauge4] ,style=dict(display='inline-block',backgroundColor='#082255' , height='330px'
                                                           ,marginLeft='100px',marginTop='40px' ) )


gauge5_header=html.H1('Sensor 4 Pressure (Bar)',id='h5',style=dict(color='white'))
gauge5_header_div=html.Div([gauge5_header], style=dict( textAlign='center',fontSize=14,marginTop='-70px'))
gauge5= daq.Gauge( showCurrentValue=False,units="BAR",  id='my-gauge5',
        label=dict(label='{}'.format(p),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px')),
        labelPosition='bottom', value=p ,min=0,max=7, color= "#42C4F7", size=270
    )
gauge5_div=html.Div([gauge5_header_div,gauge5] ,style=dict(display='inline-block',backgroundColor='#082255' , height='330px'
                                                           ,marginLeft='150px',marginTop='40px' ) )

gauge6_header=html.H1('Sensor 5 Pressure (Bar)',id='h6',style=dict(color='white'))
gauge6_header_div=html.Div([gauge6_header], style=dict( textAlign='center',fontSize=14,marginTop='-70px'))
gauge6= daq.Gauge( showCurrentValue=False,units="BAR",  id='my-gauge6',
        label=dict(label='{}'.format(p),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px')),
        labelPosition='bottom', value=p ,min=0,max=7, color= "#42C4F7", size=270
    )
gauge6_div=html.Div([gauge6_header_div,gauge6] ,style=dict(display='inline-block',backgroundColor='#082255' , height='330px'
                                                           ,marginLeft='100px',marginTop='40px' ) )

gauge7_header=html.H1('Sensor 6 Pressure (Bar)',id='h7',style=dict(color='white'))
gauge7_header_div=html.Div([gauge7_header], style=dict( textAlign='center',fontSize=14,marginTop='-70px'))
gauge7= daq.Gauge( showCurrentValue=False,units="BAR",  id='my-gauge7',
        label=dict(label='{}'.format(p),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px')),
        labelPosition='bottom', value=p ,min=0,max=7, color= "#42C4F7", size=270
    )
gauge7_div=html.Div([gauge7_header_div,gauge7] ,style=dict(display='inline-block',backgroundColor='#082255' , height='330px'
                                                           ,marginLeft='100px',marginTop='40px' ) )


sensors_menu=  dcc.Dropdown(
        id='dropdown',
        options=[
            dict(label='Sensor 1', value='s1'), dict(label='Sensor 2', value='s2'),dict(label='Sensor 3', value='s3'),
            dict(label='Sensor 4', value='s4'),dict(label='Sensor 5', value='s5'),dict(label='Sensor 6', value='s6'),
            dict(label='Sensor 7', value='s7'), dict(label='All Sensors', value='All')
        ],
        value='s1' , style=dict(color='black',fontWeight='bold',textAlign='center',height='50px')
    )
sensors_menu_div= html.Div([sensors_menu], style=dict( width='12%', marginLeft='1520px' , marginTop='-400px',fontSize=26,
                                                       border='20px solid #082255'     ))
main_header=html.H1('Remote Pressure Monitoring System',id='pms',style=dict(color='white',fontSize=28))
main_header_div= html.Div([main_header], style=dict( textAlign='center'))
np.random.seed(99)

layout=go.Layout( xaxis= dict(title= 'Time',range=[min(x),max(x)]) ,
                  yaxis= dict(title= 'Sensor readings',range=[0,7])
                 ,plot_bgcolor= 'skyblue', paper_bgcolor= 'black',font=dict(color='skyblue'))
graph=  dcc.Graph(id='my_graph' , animate=False ,config={
        'displayModeBar': True
    })
graph_div=html.Div([graph] , style=dict(width='75%', marginTop='40px',
                                                     marginLeft='50px'))

button=html.Button(   'On/Off',  id='my_button', n_clicks=0
                            ,style=dict(width='100%', fontSize=22 ,height='50px'
                         )
    )

button_div=html.Div(button,style=dict(marginTop='-50px',marginLeft='1300px',width='7%',border= '4px solid #42C4F7'))
page_location=dcc.Location(id='url', refresh=False, pathname='/page-1')
page1_link=html.Div(  dcc.Link('Prev. Page', href='/page-1',style=dict(color='blue',fontSize=40,fontWeight='bold') ,id='page1'),
             style=dict(marginTop='230px' ,backgroundColor="white",width='10%',marginLeft='1570px',border= '4px solid #42C4F7',height='50px') )

page2_link=html.Div(  dcc.Link('Next Page', href='/page-2' ,style=dict(fontSize=40
                                                , color="blue",fontWeight='bold' ,backgroundColor="white") , id='page2')
               ,style=dict(marginTop='70px' ,backgroundColor="white",width='9.5%',marginLeft='1600px',border= '4px solid #42C4F7',height='55px'))

hidden_div=html.Div(id='hidden',style=dict(display='none'))
interval1=dcc.Interval(id="timing",interval=500,n_intervals=0)
interval2=dcc.Interval(id="timing2",interval=1000,n_intervals=0)
interval5=dcc.Interval(id="timing4",interval=1000,n_intervals=0)

shaping_input=daq.NumericInput( label=dict(label='shaping sensor',style=dict(color='white',fontSize=18)),
labelPosition='top', value=pr1, min=0,max=10 ,size=100 , id='shaping'
)
shaping_input_div=html.Div([shaping_input],style=dict(marginBottom='0px',marginLeft='1250px'))

timer=daq.LEDDisplay(
    id='my-LED-display',
    label=dict(label="Cycle Timer",style=dict(color='white',fontWeight='bold',fontSize=20)),
    value=0 , size=110 , color="#42C4F7"
)
timer_div=html.Div(timer,style=dict(marginLeft='1200px',marginTop='-300px',display='block'))
app.layout =html.Div([
page_location, html.Div( [],id='outer div' ),

]  ,style=dict(backgroundColor="#061E44",height='1100px', width='1920px' , marginTop='-20px',marginLeft='-10px'

)      )
#082255
# 1267






@app.callback([Output("my-gauge","label"),Output("my-gauge2","label"),Output("my-gauge3","label"),
               Output("my-gauge4","label"),Output("my-gauge5","label"),Output("my-gauge6","label"),Output("my-gauge7","label"),
               Output("my-gauge","value"),Output("my-gauge2","value"),Output("my-gauge3","value"),Output("my-gauge4","value")
               ,Output("my-gauge5","value"),Output("my-gauge6","value"),Output("my-gauge7","value")]
             ,[Input("timing","n_intervals") ,Input("shaping","value")]
             )

def update_gauges(n_intervals,shaping_value):
    global system_state, idle,cycle_running,cycle_finished ,pr1,pr2,pr3,pr4,pr5,pr6,pr7,counter,state_trans
    if system_state==idle:
        pr1 = shaping_value
        pr2 = 0
        pr3 = 0
        pr4 = 0
        pr5 = 0
        pr6 = 0
        pr7 = 0
        if pr1>0:
            system_state=cycle_running
        return ( dict(label='{}'.format(pr1),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                , dict(label='{}'.format(pr2),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 , dict(label='{}'.format(pr3),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 , dict(label='{}'.format(pr4),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 ,dict(label='{}'.format(pr5),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 , dict(label='{}'.format(pr6),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 , dict(label='{}'.format(pr7),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 ,pr1,pr2,pr3,pr4,pr5,pr6,pr7)
    elif system_state==cycle_running:
        pr1 = shaping_value
        pr2 = np.random.randint(3, 4)
        pr3 = np.random.randint(2, 4)
        pr4 = np.random.randint(4, 6)
        pr5 = np.random.randint(1, 3)
        pr6 = np.random.randint(3, 7)
        pr7 = np.random.randint(2, 6)
        if pr1==0:
            system_state=cycle_finished
            now = datetime.now()
            name=now.strftime("%Y-%m-%d %H-%M-%S")
            book = load_workbook('PMS_Report.xlsx')
            xlwriter=pd.ExcelWriter('PMS_Report.xlsx')
            xlwriter.book = book
            df = pd.DataFrame({'time(s)': list(x), 's1(bar)': list(y1), 's2(bar)': list(y2),'s3(bar)': list(y3),
                               's4(bar)': list(y4),'s5(bar)': list(y5),'s6(bar)': list(y6),'s7(bar)': list(y7)})
            df.to_excel(xlwriter, index=False,sheet_name=name)
            xlwriter.save()
            xlwriter.close()
            writer = pd.ExcelWriter('/home/mazen/flash.xlsx')
            writer.book = book
            df.to_excel('/home/mazen/flash.xlsx')
            writer.save()


        return ( dict(label='{}'.format(pr1),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                , dict(label='{}'.format(pr2),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 , dict(label='{}'.format(pr3),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 , dict(label='{}'.format(pr4),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 ,dict(label='{}'.format(pr5),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 , dict(label='{}'.format(pr6),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 , dict(label='{}'.format(pr7),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 ,pr1,pr2,pr3,pr4,pr5,pr6,pr7)
    elif system_state== cycle_finished:
        pr1 = shaping_value
        if pr1>0:
            system_state=cycle_running
            counter=0
            x.clear()
            x.append(0)
            y1.clear()
            y1.append(0)
            y2.clear()
            y2.append(0)
            y3.clear()
            y3.append(0)
            y4.clear()
            y4.append(0)
            y5.clear()
            y5.append(0)
            y6.clear()
            y6.append(0)
            y7.clear()
            y7.append(0)


        return (dict(label='{}'.format(pr1),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                , dict(label='{}'.format(pr2),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 , dict(label='{}'.format(pr3),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 , dict(label='{}'.format(pr4),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 ,dict(label='{}'.format(pr5),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 , dict(label='{}'.format(pr6),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                 , dict(label='{}'.format(pr7),style=dict(color='#42C4F7',fontSize=60,fontStyle='bold' , marginTop='20px'))
                ,pr1,pr2,pr3,pr4,pr5,pr6,pr7)

@app.callback( [Output("hidden","children"),Output("my-LED-display","value")]
             ,Input("timing2","n_intervals") )
def update_graph_values(n_intervals):
    global counter
    if(system_state==cycle_running):
        counter+=1
        pr1 = np.random.randint(1, 3)
        pr2 = np.random.randint(3, 4)
        pr3 = np.random.randint(2, 4)
        pr4 = np.random.randint(4, 6)
        pr5 = np.random.randint(1, 3)
        pr6 = np.random.randint(3, 7)
        pr7 = np.random.randint(2, 6)

        y1.append(pr1)
        y2.append(pr2)
        y3.append(pr3)
        y4.append(pr4)
        y5.append(pr5)
        y6.append(pr6)
        y7.append(pr7)
        x.append(x[-1] + 1)

        return ("",counter)
    elif system_state==cycle_finished:
        return ("",counter)
    return("",0)


@app.callback(Output("my_graph","figure")
             ,[Input("timing4","n_intervals"),
               Input('dropdown','value') , Input("shaping","value")
               ]
             )

def update_graph_scatter(n_intervals,sensor_num,shaping_value):
    global x , pr1,pr2,pr3,pr4 ,pr5,pr6,pr7, y1 , y2 , y3 , y4,y5,y6,y7,system_state,counter,state_trans

    if system_state==idle:

        pr1=shaping_value
        data = go.Scatter(x=list(x),  y=list(y1),
            name='Upper Left',mode='lines+markers', line=dict(color='blue')
        )

        layout = go.Layout(xaxis=dict(title='Time' ,autorange=True,rangemode='tozero' ),
                           yaxis=dict(title='Sensor readings', range=[-0.05, 7])
                           , plot_bgcolor='white', paper_bgcolor='#082255', font=dict(color='white'), height=670,
                           margin=dict(l=50, r=50, t=50, b=50))
        if pr1>0:
            system_state=cycle_running
        return {'data': [data], 'layout': layout}

    elif system_state==cycle_running:
        counter+=1
        pr1 = shaping_value
        pr2 = np.random.randint(3, 4)
        pr3 = np.random.randint(2, 3)
        pr4 = np.random.randint(4, 5)
        pr5 = np.random.randint(1, 2)
        pr6 = np.random.randint(3, 4)
        pr7 = np.random.randint(2, 3)
        y1.append(pr1)
        y2.append(pr2)
        y3.append(pr3)
        y4.append(pr4)
        y5.append(pr5)
        y6.append(pr6)
        y7.append(pr7)
        x.append(x[-1] + 1)
        if pr1==0:
            system_state=cycle_finished
            df = pd.DataFrame({'time(s)': list(x), 's1(bar)': list(y1), 's2(bar)': list(y2),'s3(bar)': list(y3),
                               's4(bar)': list(y4),'s5(bar)': list(y5),'s6(bar)': list(y6),'s7(bar)': list(y7)})
            df.to_excel('Report.xlsx', index=False)


        if sensor_num== 's1':
            data = go.Scatter(
        x=list(x),
        y=list(y1),
        name='Upper Left',
        mode='lines+markers',
        line=dict(color='blue')
         )

            layout=go.Layout( xaxis= dict(title= 'Time'  , autorange=True,rangemode='tozero' ),
                  yaxis= dict(title= 'Sensor readings',range=[-0.05,7])
                 ,plot_bgcolor= 'white', paper_bgcolor= '#082255',font=dict(color='white'),height=670,margin=dict(l=50, r=50, t=50, b=50))

            return { 'data': [data], 'layout': layout }

        elif sensor_num == 's2':

            data = go.Scatter(
            x=list(x),
            y=list(y2),
            name='Down Left',
            mode='lines+markers',
            line=dict(color='red')
        )
            layout=go.Layout( xaxis= dict(title= 'Time' , autorange=True,rangemode='tozero'),
                  yaxis= dict(title= 'Sensor readings',range=[-0.05,7])
                 ,plot_bgcolor= 'white', paper_bgcolor= '#082255',font=dict(color='white'),height=670,margin=dict(l=50, r=50, t=50, b=50))
            return {'data': [data], 'layout': layout}

        elif sensor_num == 's3':

            data = go.Scatter(
            x=list(x),
            y=list(y3),
            name='Down Right',
            mode='lines+markers',
            line = dict(color='#42C4F7')
        )
            layout=go.Layout( xaxis= dict(title= 'Time', autorange=True,rangemode='tozero'),
                  yaxis= dict(title= 'Sensor readings',range=[-0.05,7])
                 ,plot_bgcolor= 'white', paper_bgcolor= '#082255',font=dict(color='white'),height=670,margin=dict(l=50, r=50, t=50, b=50))
            return {'data': [data], 'layout': layout}

        elif sensor_num == 's4':

            data = go.Scatter(
            x=list(x),
            y=list(y4),
            name='Upper Right',
            mode='lines+markers',
            line=dict(color='orange')
        )
            layout=go.Layout( xaxis= dict(title= 'Time',autorange=True,rangemode='tozero' ),
                  yaxis= dict(title= 'Sensor readings',range=[-0.05,7])
                 ,plot_bgcolor= 'white', paper_bgcolor= '#082255',font=dict(color='white'),height=670,margin=dict(l=50, r=50, t=50, b=50))
            return {'data': [data], 'layout': layout }
        elif sensor_num == 's5':

            data = go.Scatter(
            x=list(x),
            y=list(y5),
            name='Upper Right',
            mode='lines+markers',
            line=dict(color='yellow')
        )
            layout = go.Layout(xaxis=dict(title='Time', autorange=True,rangemode='tozero'),
                           yaxis=dict(title='Sensor readings', range=[-0.05, 7])
                           , plot_bgcolor='white', paper_bgcolor='#082255', font=dict(color='white'), height=670,
                           margin=dict(l=50, r=50, t=50, b=50))
            return {'data': [data], 'layout': layout}
        elif sensor_num == 's6':

            data = go.Scatter(
            x=list(x),
            y=list(y6),
            name='Upper Right',
            mode='lines+markers',
            line=dict(color='black')
        )
            layout = go.Layout(xaxis=dict(title='Time', autorange=True,rangemode='tozero'),
                           yaxis=dict(title='Sensor readings', range=[-0.05, 7])
                           , plot_bgcolor='white', paper_bgcolor='#082255', font=dict(color='white'), height=670,
                           margin=dict(l=50, r=50, t=50, b=50))
            return {'data': [data], 'layout': layout}
        elif sensor_num == 's7':

            data = go.Scatter(
            x=list(x),
            y=list(y7),
            name='Upper Right',
            mode='lines+markers',
            line=dict(color='green')
        )
            layout = go.Layout(xaxis=dict(title='Time', autorange=True,rangemode='tozero'),
                           yaxis=dict(title='Sensor readings', range=[-0.05, 7])
                           , plot_bgcolor='white', paper_bgcolor='#082255', font=dict(color='white'), height=670,
                           margin=dict(l=50, r=50, t=50, b=50))
            return {'data': [data], 'layout': layout}
        elif sensor_num == 'All':
            trace1=go.Scatter(
        x=list(x),
        y=list(y1),
        name='Shaping',
        mode='lines+markers',
        line=dict(color='blue')
         )
            trace2=go.Scatter(
            x=list(x),
            y=list(y2),
            name='Sensor1',
            mode='lines+markers',
            line=dict(color='red'))
            trace3=go.Scatter(
            x=list(x),
            y=list(y3),
            name='Sensor2',
            mode='lines+markers',
            line = dict(color="#42C4F7"))
            trace4=go.Scatter(
            x=list(x),
            y=list(y4),
            name='Sensor3',
            mode='lines+markers',
            line=dict(color='orange'))
            trace5 = go.Scatter(
            x=list(x),
            y=list(y5),
            name='Sensor4',
            mode='lines+markers',
            line=dict(color='violet'))

            trace6 = go.Scatter(
            x=list(x),
            y=list(y6),
            name='Sensor5',
            mode='lines+markers',
            line=dict(color='black'))
            trace7 = go.Scatter(
            x=list(x),
            y=list(y7),
            name='Sensor6',
            mode='lines+markers',
            line=dict(color='green'))
            layout = go.Layout(xaxis=dict(title='Time', autorange=True,rangemode='tozero'),
                           yaxis=dict(title='Sensor readings', range=[-0.05, 7])
                           , plot_bgcolor='white', paper_bgcolor='#082255', font=dict(color='white'), height=670,
                           margin=dict(l=50, r=50, t=50, b=50))
            data=[trace5,trace6,trace7,trace1,trace2,trace3,trace4]
            state_trans=True
            return {'data': data, 'layout': layout}
    elif system_state==cycle_finished:
        pr1=shaping_value
        if pr1>0:
            system_state=cycle_running
            counter=0
            x.clear()
            x.append(0)
            y1.clear()
            y1.append(0)
            y2.clear()
            y2.append(0)
            y3.clear()
            y3.append(0)
            y4.clear()
            y4.append(0)
            y5.clear()
            y5.append(0)
            y6.clear()
            y6.append(0)
            y7.clear()
            y7.append(0)
        if sensor_num== 's1':
            data = go.Scatter(
        x=list(x),
        y=list(y1),
        name='Upper Left',
        mode='lines+markers',
        line=dict(color='blue')
         )

            layout=go.Layout( xaxis= dict(title= 'Time' ,autorange=True,rangemode='tozero'
                                      ),
                  yaxis= dict(title= 'Sensor readings',range=[-0.05,7])
                 ,plot_bgcolor= 'white', paper_bgcolor= '#082255',font=dict(color='white'),height=670,margin=dict(l=50, r=50, t=50, b=50))

            return { 'data': [data], 'layout': layout }

        elif sensor_num == 's2':

            data = go.Scatter(
            x=list(x),
            y=list(y2),
            name='Down Left',
            mode='lines+markers',
            line=dict(color='red')
        )
            layout=go.Layout( xaxis= dict(title= 'Time',autorange=True,rangemode='tozero'  ),
                  yaxis= dict(title= 'Sensor readings',range=[-0.05,7])
                 ,plot_bgcolor= 'white', paper_bgcolor= '#082255',font=dict(color='white'),height=670,margin=dict(l=50, r=50, t=50, b=50))
            return {'data': [data], 'layout': layout}

        elif sensor_num == 's3':

            data = go.Scatter(
            x=list(x),
            y=list(y3),
            name='Down Right',
            mode='lines+markers',
            line = dict(color='#42C4F7')
        )
            layout=go.Layout( xaxis= dict(title= 'Time',autorange=True,rangemode='tozero'  ),
                  yaxis= dict(title= 'Sensor readings',range=[-0.05,7])
                 ,plot_bgcolor= 'white', paper_bgcolor= '#082255',font=dict(color='white'),height=670,margin=dict(l=50, r=50, t=50, b=50))
            return {'data': [data], 'layout': layout}

        elif sensor_num == 's4':

            data = go.Scatter(
            x=list(x),
            y=list(y4),
            name='Upper Right',
            mode='lines+markers',
            line=dict(color='orange')
        )
            layout=go.Layout( xaxis= dict(title= 'Time',autorange=True,rangemode='tozero'  ),
                  yaxis= dict(title= 'Sensor readings',range=[-0.05,7])
                 ,plot_bgcolor= 'white', paper_bgcolor= '#082255',font=dict(color='white'),height=670,margin=dict(l=50, r=50, t=50, b=50))
            return {'data': [data], 'layout': layout }
        elif sensor_num == 's5':

            data = go.Scatter(
            x=list(x),
            y=list(y5),
            name='Upper Right',
            mode='lines+markers',
            line=dict(color='yellow')
        )
            layout = go.Layout(xaxis=dict(title='Time', autorange=True,rangemode='tozero'),
                           yaxis=dict(title='Sensor readings', range=[-0.05, 7])
                           , plot_bgcolor='white', paper_bgcolor='#082255', font=dict(color='white'), height=670,
                           margin=dict(l=50, r=50, t=50, b=50))
            return {'data': [data], 'layout': layout}
        elif sensor_num == 's6':

            data = go.Scatter(
            x=list(x),
            y=list(y6),
            name='Upper Right',
            mode='lines+markers',
            line=dict(color='black')
        )
            layout = go.Layout(xaxis=dict(title='Time', autorange=True,rangemode='tozero'),
                           yaxis=dict(title='Sensor readings', range=[-0.05, 7])
                           , plot_bgcolor='white', paper_bgcolor='#082255', font=dict(color='white'), height=670,
                           margin=dict(l=50, r=50, t=50, b=50))
            return {'data': [data], 'layout': layout}
        elif sensor_num == 's7':

            data = go.Scatter(
            x=list(x),
            y=list(y7),
            name='Upper Right',
            mode='lines+markers',
            line=dict(color='green')
        )
            layout = go.Layout(xaxis=dict(title='Time',autorange=True,rangemode='tozero'),
                           yaxis=dict(title='Sensor readings', range=[-0.05, 7])
                           , plot_bgcolor='white', paper_bgcolor='#082255', font=dict(color='white'), height=670,
                           margin=dict(l=50, r=50, t=50, b=50))
            return {'data': [data], 'layout': layout}
        elif sensor_num == 'All':
            trace1=go.Scatter(
        x=list(x),
        y=list(y1),
        name='Shaping',
        mode='lines+markers',
        line=dict(color='blue')
         )
            trace2=go.Scatter(
            x=list(x),
            y=list(y2),
            name='Sensor1',
            mode='lines+markers',
            line=dict(color='red'))
            trace3=go.Scatter(
            x=list(x),
            y=list(y3),
            name='Sensor2',
            mode='lines+markers',
            line = dict(color="#42C4F7"))
            trace4=go.Scatter(
            x=list(x),
            y=list(y4),
            name='Sensor3',
            mode='lines+markers',
            line=dict(color='orange'))
            trace5 = go.Scatter(
            x=list(x),
            y=list(y5),
            name='Sensor4',
            mode='lines+markers',
            line=dict(color='violet'))

            trace6 = go.Scatter(
            x=list(x),
            y=list(y6),
            name='Sensor5',
            mode='lines+markers',
            line=dict(color='black'))
            trace7 = go.Scatter(
            x=list(x),
            y=list(y7),
            name='Sensor6',
            mode='lines+markers',
            line=dict(color='green'))
            layout = go.Layout(xaxis=dict(title='Time', autorange=True,rangemode='tozero'),
                           yaxis=dict(title='Sensor readings', range=[-0.05, 7])
                           , plot_bgcolor='white', paper_bgcolor='#082255', font=dict(color='white'), height=670,
                           margin=dict(l=50, r=50, t=50, b=50))
            data=[trace5,trace6,trace7,trace1,trace2,trace3,trace4]
            if pr1==0:
                system_state=cycle_finished
            return {'data': data, 'layout': layout}

@app.callback(Output('outer div', 'children'),
              [Input('url', 'pathname')])
def change_page(link_name):
    shaping_input = daq.NumericInput(label=dict(label='shaping sensor', style=dict(color='white', fontSize=22)),
                                     labelPosition='top', value=pr1, min=0, max=10, size=120, id='shaping'
                                     )
    shaping_input_div = html.Div([shaping_input], style=dict(marginTop='50px', marginLeft='1250px'))
    if link_name=="/page-2" :
        return[main_header_div,graph_div,sensors_menu_div,shaping_input_div,interval5,page1_link]

    elif link_name=="/page-1" :

        return[main_header_div,gauge1_div,gauge2_div,gauge3_div,gauge4_div,shaping_input_div,
               gauge5_div,gauge6_div,gauge7_div,timer_div,interval1,interval2,page2_link,hidden_div]
if __name__ == '__main__':
    app.run_server()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
