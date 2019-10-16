# coding: utf-8

from __future__ import absolute_import
from validationService.conf import AUTH_URL

from flask import json
from six import BytesIO
from flask import request
import requests

from validationService.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_validate_401(self):
        """Test case for Invalid token

        
        """

        token= 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI5NWFPMHJCaHJtSXdtelVJTFhMUDYyRjVIdjNGVktaa2QtWWU2S21TbFl3In0.eyJqdGkiOiI4MmEwZGRhNC1jMzYxLTQ2OWItYmNlZi03NDU2ODIxYTEzMWIiLCJleHAiOjE1NzEwODc5NzcsIm5iZiI6MCwiaWF0IjoxNTcxMDg2MTc3LCJpc3MiOiJodHRwOi8vYTkwNTQ1N2E1ZWQ4YTExZTliZWU1MDJmMzljNmNhMmQtMzQwODgwNjMxLnVzLXdlc3QtMi5lbGIuYW1hem9uYXdzLmNvbS9hdXRoL3JlYWxtcy9USEFUQy1TTVMiLCJhdWQiOlsicmVhbG0tbWFuYWdlbWVudCIsImFjY291bnQiXSwic3ViIjoiZDhhZjU5NWItYjg5MC00MWJkLThmM2ItZjVlMDBkOWExMzg5IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoidGMtaGNpLWNsaWVudCIsImF1dGhfdGltZSI6MCwic2Vzc2lvbl9zdGF0ZSI6ImRiY2JlY2Y0LWEwNjAtNGU5Ny1hOTRhLTYyYjZiZmY5MzkyMSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsiY3JlYXRlLWNsaWVudCIsInZpZXctdXNlcnMiLCJ2aWV3LWNsaWVudHMiLCJtYW5hZ2UtYXV0aG9yaXphdGlvbiIsInF1ZXJ5LWNsaWVudHMiLCJtYW5hZ2UtY2xpZW50cyIsInF1ZXJ5LWdyb3VwcyIsInF1ZXJ5LXVzZXJzIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJhZG1pbiBmaXJzdCBhZG1pbiBsYXN0IiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW5fc21zIiwiZ2l2ZW5fbmFtZSI6ImFkbWluIGZpcnN0IiwibW9iaWxlX251bWJlciI6IjcwMzM0NTY3NjgiLCJmYW1pbHlfbmFtZSI6ImFkbWluIGxhc3QiLCJlbWFpbCI6ImFkbWluX3Ntc0BnbWFpbC5jb20ifQ.g-HQIKziXx8Pql3jIQe3oPKhPaBqspy1aVKvUZk18JslasAWn-nS-sd55ehbMx_3MpL2BJbonyGL9mGYwRfekEpwj0VXMdECmPxQ8ZYElG0OGMT2_3SxugAky7xPIgTjfJhAbOzRTaaGDWNZx1ZqiOxFYIOZnKt31XFG8Ovc27gbXuRGeh9e4COrsFDmDPqMJDyUSaX-zLmyCxtZ2Ykpayltjzbtvs3EILnx7_VvNnPHeJ-fofwFnMNWUq6lr8vNePzTwVObya8J20wPqYACWVo_IVvwtImNjDpyRDDyJ6srqj0prY2bIGK2dqB_qJ-tLvx3yIiBy_xFmA8HcaQ2jQ'
        headers = {
            'Authorization': token
        }
        response = self.client.open(
            'http://localhost:8080/validate',
            method='GET',
            headers=headers)
        self.assert401(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validate_404(self):
        """Test case for bad URL


        """

        token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI5NWFPMHJCaHJtSXdtelVJTFhMUDYyRjVIdjNGVktaa2QtWWU2S21TbFl3In0.eyJqdGkiOiI4MmEwZGRhNC1jMzYxLTQ2OWItYmNlZi03NDU2ODIxYTEzMWIiLCJleHAiOjE1NzEwODc5NzcsIm5iZiI6MCwiaWF0IjoxNTcxMDg2MTc3LCJpc3MiOiJodHRwOi8vYTkwNTQ1N2E1ZWQ4YTExZTliZWU1MDJmMzljNmNhMmQtMzQwODgwNjMxLnVzLXdlc3QtMi5lbGIuYW1hem9uYXdzLmNvbS9hdXRoL3JlYWxtcy9USEFUQy1TTVMiLCJhdWQiOlsicmVhbG0tbWFuYWdlbWVudCIsImFjY291bnQiXSwic3ViIjoiZDhhZjU5NWItYjg5MC00MWJkLThmM2ItZjVlMDBkOWExMzg5IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoidGMtaGNpLWNsaWVudCIsImF1dGhfdGltZSI6MCwic2Vzc2lvbl9zdGF0ZSI6ImRiY2JlY2Y0LWEwNjAtNGU5Ny1hOTRhLTYyYjZiZmY5MzkyMSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsiY3JlYXRlLWNsaWVudCIsInZpZXctdXNlcnMiLCJ2aWV3LWNsaWVudHMiLCJtYW5hZ2UtYXV0aG9yaXphdGlvbiIsInF1ZXJ5LWNsaWVudHMiLCJtYW5hZ2UtY2xpZW50cyIsInF1ZXJ5LWdyb3VwcyIsInF1ZXJ5LXVzZXJzIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJhZG1pbiBmaXJzdCBhZG1pbiBsYXN0IiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW5fc21zIiwiZ2l2ZW5fbmFtZSI6ImFkbWluIGZpcnN0IiwibW9iaWxlX251bWJlciI6IjcwMzM0NTY3NjgiLCJmYW1pbHlfbmFtZSI6ImFkbWluIGxhc3QiLCJlbWFpbCI6ImFkbWluX3Ntc0BnbWFpbC5jb20ifQ.g-HQIKziXx8Pql3jIQe3oPKhPaBqspy1aVKvUZk18JslasAWn-nS-sd55ehbMx_3MpL2BJbonyGL9mGYwRfekEpwj0VXMdECmPxQ8ZYElG0OGMT2_3SxugAky7xPIgTjfJhAbOzRTaaGDWNZx1ZqiOxFYIOZnKt31XFG8Ovc27gbXuRGeh9e4COrsFDmDPqMJDyUSaX-zLmyCxtZ2Ykpayltjzbtvs3EILnx7_VvNnPHeJ-fofwFnMNWUq6lr8vNePzTwVObya8J20wPqYACWVo_IVvwtImNjDpyRDDyJ6srqj0prY2bIGK2dqB_qJ-tLvx3yIiBy_xFmA8HcaQ2jQ'
        headers = {
            'Authorization': token
        }
        response = self.client.open(
            'http://localhost:8080/velidate',
            method='GET',
            headers=headers)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validate_404(self):
        """Test case for bad URL


        """

        token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI5NWFPMHJCaHJtSXdtelVJTFhMUDYyRjVIdjNGVktaa2QtWWU2S21TbFl3In0.eyJqdGkiOiI4MmEwZGRhNC1jMzYxLTQ2OWItYmNlZi03NDU2ODIxYTEzMWIiLCJleHAiOjE1NzEwODc5NzcsIm5iZiI6MCwiaWF0IjoxNTcxMDg2MTc3LCJpc3MiOiJodHRwOi8vYTkwNTQ1N2E1ZWQ4YTExZTliZWU1MDJmMzljNmNhMmQtMzQwODgwNjMxLnVzLXdlc3QtMi5lbGIuYW1hem9uYXdzLmNvbS9hdXRoL3JlYWxtcy9USEFUQy1TTVMiLCJhdWQiOlsicmVhbG0tbWFuYWdlbWVudCIsImFjY291bnQiXSwic3ViIjoiZDhhZjU5NWItYjg5MC00MWJkLThmM2ItZjVlMDBkOWExMzg5IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoidGMtaGNpLWNsaWVudCIsImF1dGhfdGltZSI6MCwic2Vzc2lvbl9zdGF0ZSI6ImRiY2JlY2Y0LWEwNjAtNGU5Ny1hOTRhLTYyYjZiZmY5MzkyMSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsiY3JlYXRlLWNsaWVudCIsInZpZXctdXNlcnMiLCJ2aWV3LWNsaWVudHMiLCJtYW5hZ2UtYXV0aG9yaXphdGlvbiIsInF1ZXJ5LWNsaWVudHMiLCJtYW5hZ2UtY2xpZW50cyIsInF1ZXJ5LWdyb3VwcyIsInF1ZXJ5LXVzZXJzIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJhZG1pbiBmaXJzdCBhZG1pbiBsYXN0IiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW5fc21zIiwiZ2l2ZW5fbmFtZSI6ImFkbWluIGZpcnN0IiwibW9iaWxlX251bWJlciI6IjcwMzM0NTY3NjgiLCJmYW1pbHlfbmFtZSI6ImFkbWluIGxhc3QiLCJlbWFpbCI6ImFkbWluX3Ntc0BnbWFpbC5jb20ifQ.g-HQIKziXx8Pql3jIQe3oPKhPaBqspy1aVKvUZk18JslasAWn-nS-sd55ehbMx_3MpL2BJbonyGL9mGYwRfekEpwj0VXMdECmPxQ8ZYElG0OGMT2_3SxugAky7xPIgTjfJhAbOzRTaaGDWNZx1ZqiOxFYIOZnKt31XFG8Ovc27gbXuRGeh9e4COrsFDmDPqMJDyUSaX-zLmyCxtZ2Ykpayltjzbtvs3EILnx7_VvNnPHeJ-fofwFnMNWUq6lr8vNePzTwVObya8J20wPqYACWVo_IVvwtImNjDpyRDDyJ6srqj0prY2bIGK2dqB_qJ-tLvx3yIiBy_xFmA8HcaQ2jQ'
        headers = {
            'Authorization': token
        }
        response = self.client.open(
            'http://localhost:8080/velidate',
            method='GET',
            headers=headers)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validate_405(self):
        """Test case for bad URL


        """

        token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI5NWFPMHJCaHJtSXdtelVJTFhMUDYyRjVIdjNGVktaa2QtWWU2S21TbFl3In0.eyJqdGkiOiI4MmEwZGRhNC1jMzYxLTQ2OWItYmNlZi03NDU2ODIxYTEzMWIiLCJleHAiOjE1NzEwODc5NzcsIm5iZiI6MCwiaWF0IjoxNTcxMDg2MTc3LCJpc3MiOiJodHRwOi8vYTkwNTQ1N2E1ZWQ4YTExZTliZWU1MDJmMzljNmNhMmQtMzQwODgwNjMxLnVzLXdlc3QtMi5lbGIuYW1hem9uYXdzLmNvbS9hdXRoL3JlYWxtcy9USEFUQy1TTVMiLCJhdWQiOlsicmVhbG0tbWFuYWdlbWVudCIsImFjY291bnQiXSwic3ViIjoiZDhhZjU5NWItYjg5MC00MWJkLThmM2ItZjVlMDBkOWExMzg5IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoidGMtaGNpLWNsaWVudCIsImF1dGhfdGltZSI6MCwic2Vzc2lvbl9zdGF0ZSI6ImRiY2JlY2Y0LWEwNjAtNGU5Ny1hOTRhLTYyYjZiZmY5MzkyMSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsiY3JlYXRlLWNsaWVudCIsInZpZXctdXNlcnMiLCJ2aWV3LWNsaWVudHMiLCJtYW5hZ2UtYXV0aG9yaXphdGlvbiIsInF1ZXJ5LWNsaWVudHMiLCJtYW5hZ2UtY2xpZW50cyIsInF1ZXJ5LWdyb3VwcyIsInF1ZXJ5LXVzZXJzIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJhZG1pbiBmaXJzdCBhZG1pbiBsYXN0IiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW5fc21zIiwiZ2l2ZW5fbmFtZSI6ImFkbWluIGZpcnN0IiwibW9iaWxlX251bWJlciI6IjcwMzM0NTY3NjgiLCJmYW1pbHlfbmFtZSI6ImFkbWluIGxhc3QiLCJlbWFpbCI6ImFkbWluX3Ntc0BnbWFpbC5jb20ifQ.g-HQIKziXx8Pql3jIQe3oPKhPaBqspy1aVKvUZk18JslasAWn-nS-sd55ehbMx_3MpL2BJbonyGL9mGYwRfekEpwj0VXMdECmPxQ8ZYElG0OGMT2_3SxugAky7xPIgTjfJhAbOzRTaaGDWNZx1ZqiOxFYIOZnKt31XFG8Ovc27gbXuRGeh9e4COrsFDmDPqMJDyUSaX-zLmyCxtZ2Ykpayltjzbtvs3EILnx7_VvNnPHeJ-fofwFnMNWUq6lr8vNePzTwVObya8J20wPqYACWVo_IVvwtImNjDpyRDDyJ6srqj0prY2bIGK2dqB_qJ-tLvx3yIiBy_xFmA8HcaQ2jQ'
        headers = {
            'Authorization': token
        }
        response = self.client.open(
            'http://localhost:8080/validate',
            method='POST',
            headers=headers)
        self.assert405(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    # def test_validate_200(self):
    #     """Test case for Invalid token
    #
    #
    #     """
    #
    #     token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJUYUgxaXRxbGJMT0hnOWpUSG1peDZkbXowTWFJOWZlVU9SYmJmdzhjeXJZIn0.eyJqdGkiOiI3YWEwYTkxYS01NDIyLTRmMTUtYjYwZi00YjVhMjg0MTg0NmEiLCJleHAiOjE1NzExNTY5OTMsIm5iZiI6MCwiaWF0IjoxNTcxMTU1MTkzLCJpc3MiOiJodHRwOi8vYTkwNTQ1N2E1ZWQ4YTExZTliZWU1MDJmMzljNmNhMmQtMzQwODgwNjMxLnVzLXdlc3QtMi5lbGIuYW1hem9uYXdzLmNvbS9hdXRoL3JlYWxtcy9USEFUQy1PVFAiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiZWRiZGY5OWMtY2M1YS00Y2Y1LTlhNmEtNTQ3MDFjNjQwM2JlIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoidGMtaGNpLU9UUC1jbGllbnQiLCJhdXRoX3RpbWUiOjAsInNlc3Npb25fc3RhdGUiOiIxNGY3OGQxOC0xNjc1LTRiZTgtOGFkZi00MjQyZjFlYTUyMjAiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIioiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJKb2huIFNtaXRoIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGVzdG90cCIsImdpdmVuX25hbWUiOiJKb2huIiwibW9iaWxlX251bWJlciI6IjcwNDU2Nzg5ODYiLCJmYW1pbHlfbmFtZSI6IlNtaXRoIiwiZW1haWwiOiJqc21pdGg5OUBnbWFpbC5jb20ifQ.aZm49bEPRx82r1PRpTZXOmU8P4jMWWXjQwt3zMVa80DIUsAo4H2d5KNGa-MH7eAQgqnTUHY3gLUGsr4t2aTe0gGbd-pQqSFkxfnu8p6-SHJekmHcO2ojIZ0pkbMa0jIkqhsQFS8uygDkozjuOyXlTN3zPMQouNR1Tb4hbXP2TH_cwfZNJ3FgpM6EDxdP3bbb7Wrm6ejScUofnqIjEHFU1CipcUKbXw5foAAlMF_tCJooxu-KziPI0-eMS6R3VSK9pWIrCLhnt8sk1v2_6BsIfEXmZPHYmPuiyvgN1aepkVzLigu6-hUpT1TCnklEbqaUWT2BEcRKQMMKwlOUsXaUfA'
    #     headers = {
    #         'Authorization': token
    #     }
    #     response = self.client.open(
    #         'http://localhost:8080/validate',
    #         method='GET',
    #         headers=headers)
    #     self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))


    def test_validate_not200(self):
        """Test case for Invalid token


        """


        token = 'Bearer JhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJUYUgxaXRxbGJMT0hnOWpUSG1peDZkbXowTWFJOWZlVU9SYmJmdzhjeXJZIn0.eyJqdGkiOiI3YWEwYTkxYS01NDIyLTRmMTUtYjYwZi00YjVhMjg0MTg0NmEiLCJleHAiOjE1NzExNTY5OTMsIm5iZiI6MCwiaWF0IjoxNTcxMTU1MTkzLCJpc3MiOiJodHRwOi8vYTkwNTQ1N2E1ZWQ4YTExZTliZWU1MDJmMzljNmNhMmQtMzQwODgwNjMxLnVzLXdlc3QtMi5lbGIuYW1hem9uYXdzLmNvbS9hdXRoL3JlYWxtcy9USEFUQy1PVFAiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiZWRiZGY5OWMtY2M1YS00Y2Y1LTlhNmEtNTQ3MDFjNjQwM2JlIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoidGMtaGNpLU9UUC1jbGllbnQiLCJhdXRoX3RpbWUiOjAsInNlc3Npb25fc3RhdGUiOiIxNGY3OGQxOC0xNjc1LTRiZTgtOGFkZi00MjQyZjFlYTUyMjAiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIioiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJKb2huIFNtaXRoIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGVzdG90cCIsImdpdmVuX25hbWUiOiJKb2huIiwibW9iaWxlX251bWJlciI6IjcwNDU2Nzg5ODYiLCJmYW1pbHlfbmFtZSI6IlNtaXRoIiwiZW1haWwiOiJqc21pdGg5OUBnbWFpbC5jb20ifQ.aZm49bEPRx82r1PRpTZXOmU8P4jMWWXjQwt3zMVa80DIUsAo4H2d5KNGa-MH7eAQgqnTUHY3gLUGsr4t2aTe0gGbd-pQqSFkxfnu8p6-SHJekmHcO2ojIZ0pkbMa0jIkqhsQFS8uygDkozjuOyXlTN3zPMQouNR1Tb4hbXP2TH_cwfZNJ3FgpM6EDxdP3bbb7Wrm6ejScUofnqIjEHFU1CipcUKbXw5foAAlMF_tCJooxu-KziPI0-eMS6R3VSK9pWIrCLhnt8sk1v2_6BsIfEXmZPHYmPuiyvgN1aepkVzLigu6-hUpT1TCnklEbqaUWT2BEcRKQMMKwlOUsXaUfA'
        headers = {
            'Authorization': token
        }
        response = self.client.open(
            'http://localhost:8080/validate',
            method='GET',
            headers=headers)
        self.assertNotEqual(response, 200)




if __name__ == '__main__':
    import unittest
    unittest.main()
