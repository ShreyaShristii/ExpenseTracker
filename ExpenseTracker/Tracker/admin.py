from django.contrib import admin
from .models import Expense
from django.http import HttpResponse
import csv


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    """
    Professional, production-ready admin configuration for Expense model.
    """

    # Columns to display in list view
    list_display = ('title', 'amount', 'category', 'date')

    # Sidebar filters
    list_filter = ('category', 'date')

    # Search bar fields
    search_fields = ('title', 'category')

    # Sort newest → oldest
    ordering = ('-date',)

    # created_at shouldn't be edited manually
    readonly_fields = ('created_at',)

    # Pagination for cleaner admin
    list_per_page = 20

    # Adds a date drill-down navigation bar at top
    date_hierarchy = 'date'

    # Organize form layout
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'amount', 'category')
        }),
        ('Additional Details', {
            'fields': ('description', 'date')
        }),
        ('System Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',),  # collapsible clean UI
        })
    )

    # Register custom actions
    actions = ['export_selected_expenses']

    def export_selected_expenses(self, request, queryset):
        """
        Export selected Expense records as CSV.
        Common real-world admin action.
        """
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=expenses_export.csv'

        writer = csv.writer(response)
        writer.writerow(['Title', 'Amount', 'Category', 'Date', 'Description'])

        for expense in queryset:
            writer.writerow([
                expense.title,
                expense.amount,
                expense.category,
                expense.date,
                expense.description or ""
            ])

        return response

    export_selected_expenses.short_description = "Export selected expenses as CSV"
