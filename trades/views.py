from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Trade
from .serializers import NewTradeSerializer, TradeSerializer
from rest_framework import status
class TradeCreateRetrieveUpdateView(APIView):
    def get(self, request, id):
        try:
            trade = Trade.objects.get(id=id)
        except Trade.DoesNotExist:
            return Response({"message": "Trade not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"message": "Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = TradeSerializer(trade)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = NewTradeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self, request, trade_id, format=None):
        trade = self.get_object(trade_id)
        serializer = NewTradeSerializer(trade, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class OrderDeliveredView(APIView):
    def post(self, request, id):
        try:
            trade = Trade.objects.get(id=id)
        except Trade.DoesNotExist:
            return Response({"message": "Trade not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"message": "Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        trade.status = 'DELIVERED'
        trade.payment_status = 'PENDING'
        trade.save()
        return Response({"message": "Trade status updated successfully"}, status=200)
    
    def get(self, request, id):
        try:
            trade = Trade.objects.get(id=id)
        except Trade.DoesNotExist:
            return Response({"message": "Trade not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"message": "Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        status = trade.status
        updated_at = trade.updated_at
        return Response({"status": status, "updated_at": updated_at}, status=200)

class OrderCancelledView(APIView):
   def post(self, request, id):
        try:
            trade = Trade.objects.get(id=id)
        except Trade.DoesNotExist:
            return Response({"message": "Trade not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"message": "Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        trade.status = 'CANCELLED'
        trade.save()
        return Response({"message": "Trade status updated successfully"}, status=200)

#Use this view to create a new order on whatever the intergalactic version of Stripe or PayPal is.   
class CreateOrderView(APIView):
    pass

class PaymentConfirmView(APIView):
    def post(self, request, id):
        try:
            trade = Trade.objects.get(id=id)
        except Trade.DoesNotExist:
            return Response({"message": "Trade not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"message": "Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        trade.payment_status = 'PAID'
        trade.save()
        return Response({"message": "Payment status updated successfully"}, status=status.HTTPS_200_OK)
