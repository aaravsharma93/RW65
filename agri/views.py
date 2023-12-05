import datetime
import json

from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from agri.forms import LocationForm, CropCycleForm, UOMForm
from agri.models import Crop, CropTask, CropCycle, PlantAnalysisCriteria, SoilAnalysis, SoilTexture, SoilTextureCriteria, SoilType, UOM, Location, PlantAnalysis, Weather
from agri.models import SoilAnalysisCriteria
import requests
## Agriculture ##

# 21e696f4e0e757c95340595f106183b3


def agriculture_home(request):
    return render(request, "agriculture/home.html")


def crop(request):
    crops = Crop.objects.all()
    context = {}
    context["crops"] = crops
    return render(request, "agriculture/crop.html", context)


def crop_add(request):
    context = {}

    uom = UOM.objects.all()
    context["uom"] = uom

    crops = Crop.objects.all()
    context["crop"] = crops

    if request.method == 'POST':
        title = request.POST["title"]
        crop_name = request.POST["crop_name"]
        scientific_name = request.POST["scientific_name"]
        crop_spacing = request.POST["crop_spacing"]
        row_spacing = request.POST["row_spacing"]
        crop_spacing_uom = request.POST["crop_spacing_uom"]
        row_spacing_uom = request.POST["row_spacing_uom"]
        type = request.POST["type"]
        category = request.POST["category"]
        target_warehouse = request.POST["target_warehouse"]
        planting_uom = request.POST["planting_uom"]
        planting_area = request.POST["planting_area"]
        yield_uom = request.POST["yield_uom"]

        task_names = request.POST.getlist("task_names[]")
        start_days = request.POST.getlist("start_days[]")
        end_days = request.POST.getlist("end_days[]")
        hms = request.POST.getlist("hms[]")
        priorities = request.POST.getlist("priorities[]")

        priorities = list(filter(None, priorities))
        hms = list(filter(None, hms))
        end_days = list(filter(None, end_days))
        start_days = list(filter(None, start_days))
        task_names = list(filter(None, task_names))

        crop = Crop.objects.create(title=title)
        crop.name = crop_name
        crop.scientific_name = scientific_name
        crop.crop_spacing = int(crop_spacing)
        crop.row_spacing = int(row_spacing)
        crop.crop_spacing_uom = crop_spacing_uom
        crop.row_spacing_uom = row_spacing_uom
        crop.type = type
        crop.category = category
        # crop.target_warehouse = target_warehouse
        crop.planting_uom = planting_uom
        crop.planting_area = planting_area
        crop.yield_uom = yield_uom
        crop.save()

        # all_uom = UOM.objects.all()
        # all_uom = [str(i.name).lower() for i in all_uom]

        # new_uom = [yield_uom,planting_uom,crop_spacing_uom,row_spacing_uom]

        # for i in new_uom:
        #     if i.lower() not in all_uom:
        #         uom = UOM.objects.create(name=str(i.lower()))
        #         uom.save()

        for i in range(len(task_names)):
            task = CropTask.objects.create(name=task_names[i])
            task.start_day = datetime.datetime.strptime(
                start_days[i], "%Y-%m-%d")
            task.end_day = datetime.datetime.strptime(end_days[i], "%Y-%m-%d")
            task.holiday_management = hms[i]
            task.priority = priorities[i]
            task.crop_id = crop
            task.save()
        return HttpResponse("success")

    return render(request, "agriculture/crop_add.html", context)


def crop_view(request):
    context = {}

    uom = UOM.objects.all()
    context["uom"] = uom

    if request.method == "GET":
        crop_id = request.GET["crop_id"]
        crop = Crop.objects.get(id=crop_id)
        context["crop"] = crop
        crop_tasks = CropTask.objects.filter(crop_id=crop)
        context["crop_tasks"] = crop_tasks

    if request.method == 'POST':
        crop_id = request.POST["crop_id"]
        title = request.POST["title"]
        crop_name = request.POST["crop_name"]
        scientific_name = request.POST["scientific_name"]
        crop_spacing = request.POST["crop_spacing"]
        row_spacing = request.POST["row_spacing"]
        crop_spacing_uom = request.POST["crop_spacing_uom"]
        row_spacing_uom = request.POST["row_spacing_uom"]
        type = request.POST["type"]
        category = request.POST["category"]
        target_warehouse = request.POST["target_warehouse"]
        planting_uom = request.POST["planting_uom"]
        planting_area = request.POST["planting_area"]
        yield_uom = request.POST["yield_uom"]

        task_names = request.POST.getlist("task_names[]")
        start_days = request.POST.getlist("start_days[]")
        end_days = request.POST.getlist("end_days[]")
        hms = request.POST.getlist("hms[]")
        priorities = request.POST.getlist("priorities[]")
        task_ids = request.POST.getlist("task_ids[]")

        crop = Crop.objects.get(id=crop_id)
        crop.title = title
        crop.name = crop_name
        crop.scientific_name = scientific_name
        crop.crop_spacing = float(crop_spacing.replace(",", "."))
        crop.row_spacing = float(row_spacing.replace(",", "."))
        crop.crop_spacing_uom = crop_spacing_uom
        crop.row_spacing_uom = row_spacing_uom
        crop.type = type
        crop.category = category
        # crop.target_warehouse = target_warehouse
        crop.planting_uom = planting_uom
        crop.planting_area = planting_area
        crop.yield_uom = yield_uom
        crop.save()

        # all_uom = UOM.objects.all()
        # all_uom = [str(i.name).lower() for i in all_uom]

        # new_uom = [yield_uom,planting_uom,crop_spacing_uom,row_spacing_uom]

        # for i in new_uom:
        #     if i.lower() not in all_uom:
        #         uom = UOM.objects.create(name=str(i.lower()))
        #         uom.save()

        task_ids = list(filter(None, task_ids))
        priorities = list(filter(None, priorities))
        hms = list(filter(None, hms))
        end_days = list(filter(None, end_days))
        start_days = list(filter(None, start_days))
        task_names = list(filter(None, task_names))

        instance = CropTask.objects.filter(crop_id=crop)
        instance.delete()

        for i in range(len(task_names)):
            task = CropTask.objects.create(name=task_names[i])
            task.start_day = start_days[i]
            task.end_day = end_days[i]
            task.holiday_management = hms[i]
            task.priority = priorities[i]
            task.crop_id = crop
            task.save()

        return HttpResponse("success")

    return render(request, "agriculture/crop_view.html", context)


def crop_delete(request):
    if request.method == "GET":
        crop_id = request.GET["crop_id"]
        crop = Crop.objects.filter(id=crop_id)
        crop.delete()
        return redirect("/crop")


def add_uom(request):
    if request.method == "POST":
        form = UOMForm(request.POST)
        obj = form.save()
        return JsonResponse(model_to_dict(obj))


# Location CRUD
def crop_location(request):
    context = {}
    crop_locations = Location.objects.all()
    context['crop_locations'] = crop_locations
    return render(request, "agriculture/crop_location.html", context)


def crop_location_add(request):
    context = {}
    back = ""
    idd = ""
    if "back" in request.GET:
        back = request.GET["back"]
    if "id" in request.GET:
        idd = request.GET["id"]
    if request.POST:
        form = LocationForm(data=request.POST)
        if form.is_valid():
            location = form.save()
            if back == "paa":
                return redirect("/plant_analysis_add")
            elif back == "pae":
                return redirect("/plant_analysis_edit/{}".format(idd))
            elif back == "saa":
                return redirect("/soil_analysis_add")
            elif back == "sae":
                return redirect("/soil_analysis_edit/{}".format(idd))
            elif back == "sta":
                return redirect("/soil_texture_add")
            elif back == "ste":
                return redirect("/soil_texture_edit/{}".format(idd))
            else:
                return redirect("/crop_location")
        else:
            return JsonResponse(form.errors, status=400)
    form = LocationForm(data=None)
    context["form"] = form
    return render(request, "agriculture/crop_location_form.html", context)


def crop_location_edit(request, id):
    context = {}
    obj = Location.objects.get(id=id)
    if request.POST:
        form = LocationForm(instance=obj, data=request.POST)
        form.save()
        return redirect("/crop_location/")
    else:
        form = LocationForm(instance=obj)
        context["form"] = form
        return render(request, "agriculture/crop_location_form.html", context)


def crop_location_delete(request, id):
    obj = Location.objects.get(id=id)
    obj.delete()
    return redirect("/crop_location/")


# Crop Cycle CRUD

def crop_cycle_list(request):
    context = {}
    crop_cycle = CropCycle.objects.all()
    context['crop_cycle'] = crop_cycle
    return render(request, "agriculture/crop_cycle.html", context)


def crop_cycle_add(request):
    if request.POST:
        form = CropCycleForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
        else:
            return JsonResponse(form.errors, status=400)
    else:
        context = {}
        context["locations"] = Location.objects.all()
        form = CropCycleForm(data=None)
        context["form"] = form

        context["uom"] = UOM.objects.all()
        context["crops"] = Crop.objects.all()
        location_form = LocationForm(data=None)
        context["location_form"] = location_form
        context["head_name"] = "New"
        return render(request, "agriculture/crop_cycle_form.html", context)


def crop_cycle_edit(request, id):
    context = {}
    obj = CropCycle.objects.get(id=id)
    if request.POST:
        form = CropCycleForm(instance=obj, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
        else:
            return JsonResponse(form.errors, status=400)
    else:
        context["locations"] = Location.objects.all()
        form = CropCycleForm(instance=obj)
        context["form"] = form
        context["uom"] = UOM.objects.all()
        context["crops"] = Crop.objects.all()
        location_form = LocationForm(data=None)
        context["location_form"] = location_form
        context["crop_cycle"] = obj
        context["head_name"] = "Edit"
        return render(request, "agriculture/crop_cycle_form.html", context)


def plant_analysis_list(request):
    context = {}
    plant_analysis = PlantAnalysis.objects.all()
    context['plant_analysis'] = plant_analysis
    return render(request, "agriculture/plant_analysis.html", context)


def plant_analysis_add(request):
    context = {}
    context["crop"] = Crop.objects.all()
    loc = Location.objects.all()
    for i in loc:
        i.long_lat = json.dumps(i.long_lat)
    context["loc"] = loc

    if request.method == 'POST':
        loc_id = request.POST["loc_name"]
        crop_id = request.POST["crop_id"]
        # long_lat = request.POST["long_lat"]
        collection_datetime = request.POST["collection_datetime"]
        lab_datetime = request.POST["lab_datetime"]
        result_datetime = request.POST["result_datetime"]
        title_list, value_list, min_val_list, max_val_list = '', '', '', ''
        if len(request.POST["title_list"]) > 0:
            title_list = request.POST["title_list"].split(",")
            value_list = request.POST["value_list"].split(",")
            min_val_list = request.POST["min_val_list"].split(",")
            max_val_list = request.POST["max_val_list"].split(",")

        crop = Crop.objects.get(id=crop_id)
        loc = Location.objects.get(id=loc_id)

        pa = PlantAnalysis.objects.create(crop=crop)
        pa.name = 'PLA-{}-{}'.format(crop_id, pa.id)
        pa.location = loc
        pa.collection_datetime = collection_datetime
        pa.lab_test_datetime = lab_datetime
        pa.result_datetime = result_datetime
        pa.save()

        for i in range(len(title_list)):
            criteria = PlantAnalysisCriteria.objects.create(
                title=title_list[i])
            criteria.value = int(value_list[i])
            criteria.max_permissible_value = int(max_val_list[i])
            criteria.min_permissible_value = int(min_val_list[i])
            criteria.plant_analysis = pa
            criteria.save()

        return redirect("/plant_analysis")

    return render(request, "agriculture/plant_analysis_add.html", context)


def plant_analysis_edit(request, id):
    context = {}
    pa = PlantAnalysis.objects.get(id=id)
    pca = PlantAnalysisCriteria.objects.filter(plant_analysis=pa)
    context["name"] = pa.name
    context["crop"] = Crop.objects.all()
    context["pca"] = pca
    pa.location.long_lat = json.dumps(pa.location.long_lat)
    context["pa"] = pa
    loc = Location.objects.all()
    for i in loc:
        i.long_lat = json.dumps(i.long_lat)
    context["loc"] = loc
    if request.method == 'POST':
        loc_id = request.POST["loc_name"]
        crop_id = request.POST["crop_id"]
        # long_lat = request.POST["long_lat"]
        collection_datetime = request.POST["collection_datetime"]
        lab_datetime = request.POST["lab_datetime"]
        result_datetime = request.POST["result_datetime"]
        title_list, value_list, min_val_list, max_val_list = '', '', '', ''
        if len(request.POST["title_list"]) > 0:
            title_list = request.POST["title_list"].split(",")
            value_list = request.POST["value_list"].split(",")
            min_val_list = request.POST["min_val_list"].split(",")
            max_val_list = request.POST["max_val_list"].split(",")

        crop = Crop.objects.get(id=crop_id)
        loc = Location.objects.get(id=loc_id)

        pa = PlantAnalysis.objects.get(id=pca[0].plant_analysis.id)
        pa.location = loc
        pa.crop = crop
        pa.collection_datetime = collection_datetime
        pa.lab_test_datetime = lab_datetime
        pa.result_datetime = result_datetime
        pa.save()

        instance = PlantAnalysisCriteria.objects.filter(plant_analysis=pa)
        instance.delete()

        for i in range(len(title_list)):
            criteria = PlantAnalysisCriteria.objects.create(
                title=title_list[i])
            criteria.value = int(value_list[i])
            criteria.max_permissible_value = int(max_val_list[i])
            criteria.min_permissible_value = int(min_val_list[i])
            criteria.plant_analysis = pa
            criteria.save()

        return redirect("/plant_analysis")

    return render(request, "agriculture/plant_analysis_edit.html", context)


def plant_analysis_delete(request):
    pa_id = request.GET["id"]
    pa = PlantAnalysis.objects.get(id=pa_id)
    l = Location.objects.get(id=pa.location.id)
    l.delete()
    pa.delete()

    return redirect("/plant_analysis")


def soil_analysis_list(request):
    context = {}
    context["soil_analysis"] = SoilAnalysis.objects.all()
    return render(request, "agriculture/soil_analysis.html", context)


def soil_analysis_add(request):
    context = {}
    loc = Location.objects.all()
    for i in loc:
        i.long_lat = json.dumps(i.long_lat)
    context["loc"] = loc
    if request.method == 'POST':
        loc_id = request.POST["loc_name"]
        invoice_number = request.POST["invoice_number"]
        # long_lat = request.POST["long_lat"]
        collection_datetime = request.POST["collection_datetime"]
        lab_datetime = request.POST["lab_datetime"]
        result_datetime = request.POST["result_datetime"]
        title_list, value_list, min_val_list, max_val_list = '', '', '', ''
        if len(request.POST["title_list"]) > 0:
            title_list = request.POST["title_list"].split(",")
            value_list = request.POST["value_list"].split(",")
            min_val_list = request.POST["min_val_list"].split(",")
            max_val_list = request.POST["max_val_list"].split(",")

        loc = Location.objects.get(id=loc_id)

        pa = SoilAnalysis.objects.create(
            collection_datetime=collection_datetime)
        pa.name = 'SOA-{}-{}'.format(collection_datetime[:7], pa.id)
        pa.location = loc
        pa.invoice_number = invoice_number
        pa.lab_test_datetime = lab_datetime
        pa.result_datetime = result_datetime
        pa.save()

        for i in range(len(title_list)):
            criteria = SoilAnalysisCriteria.objects.create(title=title_list[i])
            criteria.value = int(value_list[i])
            criteria.max_permissible_value = int(max_val_list[i])
            criteria.min_permissible_value = int(min_val_list[i])
            criteria.soil_analysis = pa
            criteria.save()

        return redirect("/soil_analysis")
    return render(request, "agriculture/soil_analysis_add.html", context)


def soil_analysis_edit(request, id):
    context = {}
    pa = SoilAnalysis.objects.get(id=id)
    pca = SoilAnalysisCriteria.objects.filter(soil_analysis=pa)
    context["name"] = pa.name
    context["pca"] = pca
    pa.location.long_lat = json.dumps(pa.location.long_lat)
    context["pa"] = pa
    loc = Location.objects.all()
    for i in loc:
        i.long_lat = json.dumps(i.long_lat)
    context["loc"] = loc
    if request.method == 'POST':
        loc_id = request.POST["loc_name"]
        invoice_number = request.POST["invoice_number"]
        # long_lat = request.POST["long_lat"]
        collection_datetime = request.POST["collection_datetime"]
        lab_datetime = request.POST["lab_datetime"]
        result_datetime = request.POST["result_datetime"]
        title_list, value_list, min_val_list, max_val_list = '', '', '', ''
        if len(request.POST["title_list"]) > 0:
            title_list = request.POST["title_list"].split(",")
            value_list = request.POST["value_list"].split(",")
            min_val_list = request.POST["min_val_list"].split(",")
            max_val_list = request.POST["max_val_list"].split(",")

        loc = Location.objects.get(id=loc_id)

        pa = SoilAnalysis.objects.get(id=id)
        pa.invoice_number = invoice_number
        pa.location = loc
        pa.collection_datetime = collection_datetime
        pa.lab_test_datetime = lab_datetime
        pa.result_datetime = result_datetime
        pa.save()

        instance = SoilAnalysisCriteria.objects.filter(soil_analysis=pa)
        instance.delete()

        for i in range(len(title_list)):
            criteria = SoilAnalysisCriteria.objects.create(title=title_list[i])
            criteria.value = int(value_list[i])
            criteria.max_permissible_value = int(max_val_list[i])
            criteria.min_permissible_value = int(min_val_list[i])
            criteria.soil_analysis = pa
            criteria.save()

        return redirect("/soil_analysis")

    return render(request, "agriculture/soil_analysis_edit.html", context)


def soil_analysis_delete(request):
    pa_id = request.GET["id"]
    pa = SoilAnalysis.objects.get(id=pa_id)
    l = Location.objects.get(id=pa.location.id)
    l.delete()
    pa.delete()

    return redirect("/soil_analysis")


def soil_texture_list(request):
    context = {}
    context["soil_texture"] = SoilTexture.objects.all()
    return render(request, "agriculture/soil_texture.html", context)


def soil_texture_add(request):
    context = {}
    context["soil_type"] = SoilType.objects.all()
    loc = Location.objects.all()
    for i in loc:
        i.long_lat = json.dumps(i.long_lat)
    context["loc"] = loc
    if request.method == 'POST':
        loc_id = request.POST["loc_name"]
        soil_type = request.POST["soil_type"]
        clay_composition = request.POST["clay_composition"]
        sand_composition = request.POST["sand_composition"]
        silt_composition = request.POST["silt_composition"]
        # long_lat = request.POST["long_lat"]
        collection_datetime = request.POST["collection_datetime"]
        lab_datetime = request.POST["lab_datetime"]
        result_datetime = request.POST["result_datetime"]
        title_list, value_list, min_val_list, max_val_list = '', '', '', ''
        if len(request.POST["title_list"]) > 0:
            title_list = request.POST["title_list"].split(",")
            value_list = request.POST["value_list"].split(",")
            min_val_list = request.POST["min_val_list"].split(",")
            max_val_list = request.POST["max_val_list"].split(",")

        loc = Location.objects.get(id=loc_id)

        pa = SoilTexture.objects.create(
            collection_datetime=collection_datetime)
        pa.name = 'SOT-{}-{}'.format(collection_datetime[:7], pa.id)
        pa.location = loc
        if len(soil_type) > 0:
            st = SoilType.objects.get(id=soil_type)
            pa.soil_type = st
        pa.clay_composition = clay_composition
        pa.sand_composition = sand_composition
        pa.silt_composition = silt_composition
        pa.lab_test_datetime = lab_datetime
        pa.result_datetime = result_datetime
        pa.save()

        for i in range(len(title_list)):
            criteria = SoilTextureCriteria.objects.create(title=title_list[i])
            criteria.value = int(value_list[i])
            criteria.max_permissible_value = int(max_val_list[i])
            criteria.min_permissible_value = int(min_val_list[i])
            criteria.soil_texture = pa
            criteria.save()

        return redirect("/soil_texture")

    return render(request, "agriculture/soil_texture_add.html", context)


def soil_texture_edit(request, id):
    context = {}
    context["soil_type"] = SoilType.objects.all()
    pa = SoilTexture.objects.get(id=id)
    pca = SoilTextureCriteria.objects.filter(soil_texture=pa)
    context["name"] = pa.name
    context["pca"] = pca
    pa.clay_composition = str(pa.clay_composition)
    pa.sand_composition = str(pa.sand_composition)
    pa.silt_composition = str(pa.silt_composition)
    pa.location.long_lat = json.dumps(pa.location.long_lat)
    context["st"] = pa
    loc = Location.objects.all()
    for i in loc:
        i.long_lat = json.dumps(i.long_lat)
    context["loc"] = loc
    if request.method == 'POST':
        loc_id = request.POST["loc_name"]
        soil_type = request.POST["soil_type"]
        clay_composition = request.POST["clay_composition"]
        sand_composition = request.POST["sand_composition"]
        silt_composition = request.POST["silt_composition"]
        long_lat = request.POST["long_lat"]
        collection_datetime = request.POST["collection_datetime"]
        lab_datetime = request.POST["lab_datetime"]
        result_datetime = request.POST["result_datetime"]
        title_list, value_list, min_val_list, max_val_list = '', '', '', ''
        if len(request.POST["title_list"]) > 0:
            title_list = request.POST["title_list"].split(",")
            value_list = request.POST["value_list"].split(",")
            min_val_list = request.POST["min_val_list"].split(",")
            max_val_list = request.POST["max_val_list"].split(",")

        loc = Location.objects.get(id=loc_id)

        pa = SoilTexture.objects.get(id=id)
        if len(soil_type) > 0:
            st = SoilType.objects.get(id=soil_type)
            pa.soil_type = st
        pa.clay_composition = clay_composition
        pa.sand_composition = sand_composition
        pa.silt_composition = silt_composition
        pa.location = loc
        pa.collection_datetime = collection_datetime
        pa.lab_test_datetime = lab_datetime
        pa.result_datetime = result_datetime
        pa.save()

        instance = SoilTextureCriteria.objects.filter(soil_texture=pa)
        instance.delete()

        for i in range(len(title_list)):
            criteria = SoilTextureCriteria.objects.create(title=title_list[i])
            criteria.value = int(value_list[i])
            criteria.max_permissible_value = int(max_val_list[i])
            criteria.min_permissible_value = int(min_val_list[i])
            criteria.soil_texture = pa
            criteria.save()

        return redirect("/soil_texture")

    return render(request, "agriculture/soil_texture_edit.html", context)


def soil_texture_delete(request):
    pa_id = request.GET["id"]
    pa = SoilTexture.objects.get(id=pa_id)
    l = Location.objects.get(id=pa.location.id)
    l.delete()
    pa.delete()

    return redirect("/soil_texture")


def weather(request):
    context = {}
    weather_reports = Weather.objects.all()
    context["weather_reports"] = weather_reports
    return render(request, "agriculture/weather.html", context)
