# encoding=utf-8
# 实例：身体质量指数BMI
height,weight = eval(input('请输入身高和体重，用逗号隔开：'))
def getBMI(w,h):
    bmi = w / pow(h,2)
    GJ_BMI = ''
    GN_BMI = ''
    if bmi < 18.5:
        GJ_BMI = '偏瘦'
    elif bmi >= 18.5 and bmi < 25:
        GJ_BMI = '正常'
    elif bmi >= 25 and bmi < 30:
        GJ_BMI = '偏胖'
    else:
        GJ_BMI = '肥胖'
    if bmi < 18.5:
        GN_BMI = '偏瘦'
    elif bmi >= 18.5 and bmi < 24:
        GN_BMI = '正常'
    elif bmi >= 24 and bmi < 28:
        GN_BMI = '偏胖'
    else:
        GN_BMI = '肥胖'
    return 'BMI指数为：{}，国际：{}，国内：{}'.format(round(bmi,2),GJ_BMI,GN_BMI)

print(getBMI(weight,height))