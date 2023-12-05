from django.db.models import Sum
from yard import models as yard_models


def get_material_stats(dt_range):
    transactions = yard_models.Transaction.objects.filter(created_date_time__range=dt_range)
    if (len(transactions) > 0):
        top_articles = yard_models.Transaction.objects.values("article__name").annotate(
            material_weight=Sum("net_weight")).order_by("-material_weight")[:10]
        return {
            "transactions": transactions,
            "top_articles": top_articles
        }
    return None


def get_vehicle_statistics(dt_range):
    transactions = yard_models.Transaction.objects.filter(created_date_time__range=dt_range)
    if len(transactions) > 0:
        top_articles = yard_models.Transaction.objects.values("article__name","vehicle__id","vehicle__driver_name").annotate(
            material_weight=Sum("net_weight")).order_by("-material_weight")[:10]
        all_materials = yard_models.Transaction.objects.values("article", "article__name").distinct()

        top_vehicle_material = {}
        for material in all_materials:
            vehicle_mat_list = yard_models.Transaction.objects.values("vehicle__id").annotate(
                material_weight=Sum("net_weight")).filter(article=material["article"]).order_by("-material_weight")[:10]
            top_vehicle_material[material["article__name"]] = vehicle_mat_list
        print(top_vehicle_material)
        return {
            "transactions": transactions,
            "top_articles": top_articles,
            "top_vehicle_material": top_vehicle_material
        }
    return None


def get_customer_statistics(dt_range):
    transactions = yard_models.Transaction.objects.filter(created_date_time__range=dt_range)
    if len(transactions) > 0:
        top_customer = yard_models.Transaction.objects.values("customer__id","customer__name").annotate(
            material_weight=Sum("net_weight")).order_by("-material_weight")[:10]

        all_materials = yard_models.Transaction.objects.values("article", "article__name").distinct()

        top_customer_material = {}
        for material in all_materials:
            customer_mat_list = yard_models.Transaction.objects.values("customer__id","customer__name").annotate(
                material_weight=Sum("net_weight")).filter(article=material["article"]).order_by("-material_weight")[:10]
            top_customer_material[material["article__name"]] = customer_mat_list

        return {
            "transactions": transactions,
            "top_customer":top_customer,
            "top_customer_material": top_customer_material
        }
    return None


def get_supplier_statistics(dt_range):
    transactions = yard_models.Transaction.objects.filter(created_date_time__range=dt_range)
    if (len(transactions) > 0):
        return {
            "transactions": transactions
        }
    return None


def get_supplier_vehicle_stats(dt_range):
    transactions = yard_models.Transaction.objects.filter(created_date_time__range=dt_range)
    if (len(transactions) > 0):
        return {
            "transactions": transactions
        }
    return None


def get_yield_per_area_stats(dt_range):
    transactions = yard_models.Transaction.objects.filter(created_date_time__range=dt_range)
    if (len(transactions) > 0):
        return {
            "transactions": transactions
        }
    return None


field_func = {
    "material": get_material_stats,
    "vehicle": get_vehicle_statistics,
    "customer": get_customer_statistics,
    "supplier": get_supplier_statistics,
    "supplier-vehicle": get_supplier_vehicle_stats,
    "yield-per-area": get_yield_per_area_stats,
}
