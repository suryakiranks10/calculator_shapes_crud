from django.shortcuts import render
from django.views.generic import View
from json import loads
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  #to make view work without csrf tokens but only works in function
from django.utils.decorators import method_decorator  # add csrf exempt in method bcus we have class not function
# Create your views here.

@method_decorator(csrf_exempt,name="dispatch") 
class AdditionView(View):

    def post(self,request):

        json_data=request.body #here the request body is taken and got in json format we have to change it to dictionary to add num1 and num2

        form_data=loads(json_data)  #json to pynt

        n1=form_data.get("num1")

        n2=form_data.get("num2")

        result=n1+n2

        response_data={"addition_result":result}

        return JsonResponse(response_data)

    

@method_decorator(csrf_exempt,name="dispatch")
class SubtractionView(View):

    def post(self,request):

        json_data=request.body

        form_data=loads(json_data)

        n1=form_data.get("num1")

        n2=form_data.get("num2")

        result=n1-n2

        response_data={"subtraction_result":result}

        return JsonResponse(response_data)



@method_decorator(csrf_exempt,name="dispatch")
class MultiplicationView(View):

    def post(self,request):

        json_data=request.body

        form_data=loads(json_data)

        n1=form_data.get("num1")

        n2=form_data.get("num2")

        result=n1*n2

        response_data={"multiplication_result":result}

        return JsonResponse(response_data)



@method_decorator(csrf_exempt,name="dispatch")
class SquareView(View):

    def post(self,request):

        json_data=request.body

        form_data=loads(json_data)

        a=form_data.get("side")

        area=a*a

        response_data={"square_area":area}

        return JsonResponse(response_data)


@method_decorator(csrf_exempt,name="dispatch")
class RectangleView(View):

    def post(self,request):

        json_data=request.body

        form_data=loads(json_data)

        l=form_data.get("length")

        w=form_data.get("width")

        area=l*w

        response_data={"rectangle_area":area}

        return JsonResponse(response_data)


@method_decorator(csrf_exempt,name="dispatch")
class TriangleView(View):

    def post(self,request):

        json_data=request.body

        form_data=loads(json_data)

        b=form_data.get("base")

        h=form_data.get("height")

        area=1/2*b*h

        response_data={"triangle_area":area}

        return JsonResponse(response_data)


@method_decorator(csrf_exempt,name="dispatch")
class CircleView(View):

    def post(self,request):

        json_data=request.body

        form_data=loads(json_data)

        r=form_data.get("radius")

        area=3.14*r*r

        response_data={"circle_area":area}

        return JsonResponse(response_data)


@method_decorator(csrf_exempt,name="dispatch")
class ParallelogramView(View):

    def post(self,request):

        json_data=request.body

        form_data=loads(json_data)

        b=form_data.get("base")

        h=form_data.get("vertical_height")

        area=b*h

        response_data={"parallelogram_area":area}

        return JsonResponse(response_data)


@method_decorator(csrf_exempt,name="dispatch")
class TrapeziumView(View):

    def post(self,request):

        json_data=request.body

        form_data=loads(json_data)

        a=form_data.get("length_1")

        b=form_data.get("length_2")

        h=form_data.get("height")

        area=1/2*(a+b)*h

        response_data={"trapezium_area":area}

        return JsonResponse(response_data)


@method_decorator(csrf_exempt,name="dispatch")
class RhombusView(View):

    def post(self,request):

        json_data=request.body

        form_data=loads(json_data)

        b=form_data.get("base")

        h=form_data.get("height")

        area=b*h

        response_data={"rhombus_area":area}

        return JsonResponse(response_data)


@method_decorator(csrf_exempt,name="dispatch")
class EllipseView(View):

    def post(self,request):

        json_data=request.body

        form_data=loads(json_data)

        a=form_data.get("semi_major")

        b=form_data.get("semi_minor")

        area=3.14*a*b

        response_data={"ellipse_area":area}

        return JsonResponse(response_data)