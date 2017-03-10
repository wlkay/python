import rhinoscriptsyntax as rs

#must have default layer and "Source Points" initialized for this to work

source_pts = rs.ObjectsByLayer("Source Points", True)
point = rs.GetObject("select the point on default layer")
l_id = rs.LayerId("Source Points")
rs.ObjectLayer(point,l_id)
