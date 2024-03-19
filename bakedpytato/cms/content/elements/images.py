from ._elements import BaseContainerElement, BaseInlineElement


class ImageElement(BaseContainerElement):
    def __init__(
            self,
            image,
            header=None,
            caption=None
    ):
        super().__init__(self, orient='vertical')
        if header:
            self.add_child(header)
        self.add_child(image)
        if caption:
            self.add_child(caption)


class ImageHeader(BaseInlineElement):
    pass


class ImageCaption(BaseInlineElement):
    pass


class Image(BaseInlineElement):
    def __init__(self, image, alt_text):
        self.image = image
        self.alt_text = alt_text
        super().__init__(self)
