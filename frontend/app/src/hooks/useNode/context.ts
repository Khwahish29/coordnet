import { HocuspocusProvider } from "@hocuspocus/provider";
import { createContext } from "react";
import * as Y from "yjs";

import { GraphEdge, GraphNode } from "@/types";

type NodeContextType = {
  connected: boolean;
  synced: boolean;
  editorProvider: HocuspocusProvider | undefined;
  editorYdoc: Y.Doc;
  graphYdoc: Y.Doc;
  nodesMap: Y.Map<GraphNode>;
  edgesMap: Y.Map<GraphEdge>;
  nodes: GraphNode[];
  edges: GraphEdge[];
};

/**
 * Context for sharing node between components
 */
export const NodeContext = createContext<NodeContextType | undefined>(undefined);
