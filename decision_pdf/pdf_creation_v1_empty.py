from pdfrw import PdfWriter, PdfReader

import variables

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# output_pdf = variables.output_file_name + ".pdf"
# print(output_pdf)

# output_pdf ="scoring_matrix_fillable.pdf"


def create_fillable_pdf(pdf_path):

    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 50, variables.document_title['title'])

    # Score fields
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, variables.decision_parameters[0])
    c.drawString(50, height - 130, variables.decision_parameters[1])
    c.drawString(50, height - 160, variables.decision_parameters[2])
    c.drawString(50, height - 190, variables.decision_parameters[3])
    c.drawString(50, height - 220, variables.decision_parameters[4])

    c.drawString(150, height - 80, "Score (1-5):")
    form = c.acroForm
    for i in range(5):
        form.textfield(
            name=f"score{i+1}",
            x=350,
            y=height - 105 - (30 * i),
            width=50,
            height=20,
            value="",
            borderStyle='underlined',
            borderColor=None
        )

    c.drawString(50, height - 270, variables.total_score_label['total_score'])
    form.textfield(
        name=variables.total_score_label['total_score'],
        x=150,
        y=height - 275,
        width=100,
        height=20,
        value="",
        borderStyle='underlined',
        borderColor=None,
    )

    # c.drawString(50, height - 300, "Decision:")
    # form.choicefield(
    #     name="decision",
    #     x=150,
    #     y=height - 305,
    #     width=200,
    #     height=20,
    #     options=["Positive Decision", "Negative Decision", "Arbitrary Decision"],
    #     borderStyle='underlined',
    #     borderColor=None,
    #     fillColor=None,
    #     value="Arbitrary Decision"  # Default value
    # )


    c.drawString(50, height - 300, variables.prepared_by_labels['name'])
    form.textfield(
        name=variables.prepared_by_labels['name'],
        x=150,
        y=height - 305,
        width=100,
        height=20,
        value="",
        borderStyle='underlined',
        borderColor=None,
    )

    c.drawString(270, height - 300, variables.prepared_by_labels['position'])
    form.textfield(
        name=variables.prepared_by_labels['position'],
        x=350,
        y=height - 305,
        width=200,
        height=20,
        value="",
        borderStyle='underlined',
        borderColor=None,
    )

    c.drawString(50, height - 400, variables.actions_label['action'])
    form.textfield(
        name=variables.actions_label['action'],
        x=150,
        y=height - 405,
        width=200,
        height=20,
        value="",
        borderStyle='underlined',
        borderColor=None,
    )



    c.save()
#
#     def add_dropdown_to_pdf(input_pdf, output_pdf):
#         template_pdf = PdfReader(input_pdf)
#         page = template_pdf.pages[0]
#
#         # Add a dropdown menu for the "Decision" field
#         page.Annots.append({
#             '/Subtype': '/Widget',
#             '/T': 'decision',  # Name of the field
#             '/FT': '/Ch',  # Type of field: Choice (Dropdown)
#             '/F': 4,  # Flag (set to 4 for visible and printable)
#             '/Rect': [150, 250, 350, 270],  # Position of the dropdown (x, y, width, height)
#             '/V': 'Arbitrary Decision',  # Default value
#             '/Opt': [  # Options for the dropdown menu
#                 'Positive Decision',
#                 'Negative Decision',
#                 'Arbitrary Decision'
#             ],
#             '/P': page
#         })
#
#         # Save the updated PDF with the dropdown menu
#         PdfWriter(output_pdf, trailer=template_pdf).write()
#
#     # Step 3: Create PDF and Add Dropdown
#     fillable_pdf = "fillable_template.pdf"
#     create_fillable_pdf(fillable_pdf)
#
# # create_fillable_pdf(output_pdf)
# # print(f"Fillable PDF created: {output_pdf}")
#

if "__main__" == __name__:
    print("6")
    output_pdf = variables.output_file_name['name'] + ".pdf"
    print(output_pdf)
    create_fillable_pdf(output_pdf)
    print(f"Fillable PDF created: {output_pdf}")
