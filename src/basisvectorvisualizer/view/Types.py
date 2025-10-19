class Margin():
    def __init__(self, marginAll: int = None, marginLeft: int = None, marginRight: int = None, marginTop: int = None, marginBottom: int = None):
        self.marginAll = marginAll
        self.marginLeft = marginLeft
        self.marginRight = marginRight
        self.marginBottom = marginBottom
        self.marginTop = marginTop

    def getMargin(self) -> tuple[int, int, int, int]:

        if (self.marginAll):
            return (self.marginAll, self.marginAll, self.marginAll, self.marginAll)
        marginList = [0, 0, 0, 0]
        if (self.marginLeft):
            marginList[0] = self.marginLeft
        if (self.marginTop):
            marginList[1] = self.marginTop
        if (self.marginRight):
            marginList[2] = self.marginRight
        if (self.marginBottom):
            marginList[3] = self.marginBottom

        return tuple(marginList)


class Padding():
    def __init__(self, paddingAll: int = None, paddingLeft: int = None, paddingRight: int = None, paddingTop: int = None, paddingBottom: int = None):
        self.paddingAll = paddingAll
        self.paddingLeft = paddingLeft
        self.paddingRight = paddingRight
        self.paddingBottom = paddingBottom
        self.paddingTop = paddingTop

    def getPadding(self) -> str:

        if (self.paddingAll):
            return f"{self.paddingAll}px {self.paddingAll}px {self.paddingAll}px {self.paddingAll}px"
        paddingList = [0, 0, 0, 0]
        if (self.paddingTop):
            paddingList[0] = self.paddingTop
        if (self.paddingRight):
            paddingList[1] = self.paddingRight
        if (self.paddingBottom):
            paddingList[2] = self.paddingBottom
        if (self.paddingLeft):
            paddingList[3] = self.paddingLeft

        return f"{paddingList[0]}px {paddingList[1]}px {paddingList[2]}px {paddingList[3]}px"


class ToolBoxState():
    def __init__(self, plotVectors: bool, plotStandardBasisVectors: bool, plotCurrentBasisVectors: bool, drawShape: bool, fillShape: bool, fillColor: str):
        self.plotVectors = plotVectors
        self.plotStandardBasisVectors = plotStandardBasisVectors
        self.plotCurrentBasisVectors = plotCurrentBasisVectors
        self.drawShape = drawShape
        self.fillShape = fillShape
        self.fillColor = fillColor
